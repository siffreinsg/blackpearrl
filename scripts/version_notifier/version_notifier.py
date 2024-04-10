'''
Description:  Checks for new releases of apps and sends a Tautulli notification.
Author:       /u/siffreinsg
Requires:     dotenv, requests, PyYAML

Environment variables:
    * GITHUB_TOKEN - GitHub token, see https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
    * APP_CONFIG_PATH - Path to store data, default is ~/.local (version_notifier folder will be created)

Usage:
    python version_notifier.py
'''
import os
import sys
from pathlib import Path  # if you haven't already done so

import dotenv
import requests
import yaml

# Add the parent directory to the path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Import the notify function from tautulli_notify
from tautulli_notify.tautulli_notify import notify

# Load environment variables
dotenv.load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
APP_STORE_PATH = os.path.join(os.getenv('APP_CONFIG_PATH', os.path.join(os.path.expanduser('~'), '.local')), 'version_notifier')

# Static values
NOTIFICATION_SUBJECT = "<b>Version Notifier</b>"
GITHUB_HEADERS = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
GITHUB_PARAMS = {"per_page": 15}


def initiate_data_store():
    if not os.path.exists(APP_STORE_PATH): # If the directory doesn't exist
        os.mkdir(APP_STORE_PATH) # Create it
        print(f"Created data store on path '{APP_STORE_PATH}'.")
        return
    if not os.path.isdir(APP_STORE_PATH): # If not a directory
        raise Exception(f"{APP_STORE_PATH} is not a directory.") # Raise an error


def load_services():
    filepath = os.path.join(APP_STORE_PATH, "services.yaml")
    print(f"Loading services from {filepath}...")

    try:
        with open(filepath, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        raise Exception("services.yaml not found.")
    except yaml.YAMLError as e:
        raise Exception(f"Error while parsing services.yaml: {e}")
    except Exception as e:
        raise Exception(f"Error while loading services.yaml: {e}")


def get_version_file(service):
    filename = f"version-{service['label']}.txt"
    filepath = os.path.join(APP_STORE_PATH, 'versions', filename)

    if not os.path.exists(filepath):
        return None

    with open(filepath, "r") as f:
        return f.read()


def update_version_file(service, version):
    filename = f"version-{service['label']}.txt"
    filepath = os.path.join(APP_STORE_PATH, 'versions', filename)

    with open(filepath, "w") as f:
        f.write(version)


def check_app_update(service):
    repo = service['repo']
    target_commitish = service['target_commitish'] if ("target_commitish" in service) else None

    response = requests.get(
        f"https://api.github.com/repos/{repo}/releases",
        params=GITHUB_PARAMS,
        headers=GITHUB_HEADERS
    )

    if response.status_code != 200:
        raise Exception(f"Error {response.status_code} while fetching {response.url}.")

    releases = response.json()

    if target_commitish:
        releases = [release for release in releases if (release.get("target_commitish") == target_commitish)] # Get the releases for the target branch

    if len(releases) == 0:
        return None

    latest = releases[0] # Get the latest release
    last_version_notified = get_version_file(service) # Get the last version notified
    if last_version_notified != latest.get("tag_name"): # If the latest version is different from the last version notified
        return latest # Return the latest release

if __name__ == '__main__':
    initiate_data_store() # Create the data folder if it doesn't exist
    services = load_services() # Load the services to check

    for service in services: # For each service
        label, display_name, repo = service["label"], service["display_name"], service["repo"]
        print(f"Checking updates for {display_name}...")

        try:
            release = check_app_update(service)
        except Exception as e:
            print(f"Error while checking updates for {display_name}: {e}")
            notify(
                NOTIFICATION_SUBJECT,
                f"Erreur lors de la recherche de mises à jour de <b>{display_name}</b>: <pre language=\"python\">{e}</pre>"
            )
        else:
            if not release:
                print(f"No update found for {display_name}.")
                continue

            version = release.get("tag_name")
            url = release.get("html_url")
            print(f"Update found for {display_name}: {version}.")
            update_version_file(service, version)

            notify(
                NOTIFICATION_SUBJECT,
                f"Mise à jour de <b>{display_name}</b> à la version <code>{version}</code> disponible.\n{url}"
            )
