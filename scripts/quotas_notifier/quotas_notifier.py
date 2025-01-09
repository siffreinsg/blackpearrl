import datetime
import os
import sys
from pathlib import Path

import dotenv
import requests
import timeago

# Add the parent directory to the path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Import the notify function from tautulli_notify
from tautulli_notify.tautulli_notify import notify

# Load environment variables
dotenv.load_dotenv()

ULTRA_API_TOKEN = os.getenv('ULTRA_API_TOKEN')
ULTRA_API_BASEURL = os.getenv('ULTRA_API_BASEURL')
DISK_USAGE_THRESHOLD_GB = int(os.getenv('DISK_USAGE_THRESHOLD_GB', 5000))
TRAFFIC_USAGE_THRESHOLD_PERCENT = int(os.getenv('TRAFFIC_USAGE_THRESHOLD_PERCENT', 80))


def send_request(url, auth_token):
    """
    Send a GET request to the specified URL with the authorization token.

    Args:
        url (_type_): API endpoint URL.
        auth_token (_type_): Authorization token.
    """
    try:
        # Create headers with authorization token
        headers = {
            'Authorization': f'Bearer {auth_token}'
        }

        # Send a GET request with the headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to send request to {url}. Status code: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    if not ULTRA_API_TOKEN or not ULTRA_API_BASEURL:
        print("ULTRA_API_TOKEN or ULTRA_API_BASEURL environment variables not set.")
        sys.exit(1)

    url = f"{ULTRA_API_BASEURL}/total-stats"
    stats = send_request(url, ULTRA_API_TOKEN)

    if not stats:
        print("Failed to get stats.")
        sys.exit(1)

    # Disk usage
    free_storage_gb = int(stats['service_stats_info']['free_storage_gb'])
    total_storage_value = int(stats['service_stats_info']['total_storage_value'])
    used_storage_value = int(stats['service_stats_info']['used_storage_value'])

    # Traffic usage
    traffic_used_percent = round(stats['service_stats_info']['traffic_used_percentage'], 2)
    traffic_available_percent = round(stats['service_stats_info']['traffic_available_percentage'], 2)
    last_traffic_reset = stats['service_stats_info']['last_traffic_reset'].split('T')[0]
    next_traffic_reset = stats['service_stats_info']['next_traffic_reset'].split('T')[0]

    # Format the time ago string for the next traffic reset
    next_traffic_reset_in = timeago.format(next_traffic_reset, datetime.datetime.now())

    # Notify if the disk usage is above the threshold
    if free_storage_gb > DISK_USAGE_THRESHOLD_GB:
        notify(
            '<b>Disk Usage Warning</b>',
            f"Disk usage is <b>{used_storage_value} GB</b> out of <b>{total_storage_value} GB</b>.\nFree space: <b>{free_storage_gb} GB</b>."
        )

    # Notify if the traffic usage is above the threshold
    if traffic_used_percent > TRAFFIC_USAGE_THRESHOLD_PERCENT:
        notify(
            '<b>Traffic Usage Warning</b>',
            f"Traffic usage is <b>{traffic_used_percent} %</b>.\nAvailable traffic: <b>{traffic_available_percent} %</b>\nNext reset: <b>{next_traffic_reset} ({next_traffic_reset_in})</b>"
        )
