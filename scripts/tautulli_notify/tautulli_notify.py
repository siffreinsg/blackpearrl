'''
Description:  Send a Tautulli notification from command line
Author:       Siffrein SIGY <hello@siffreinsigy.com> (GitHub: siffreinsg)
Requires:     requests

Environment variables:
    * TAUTULLI_URL - Tautulli URL, e.g. http://localhost:8181
    * TAUTULLI_API_KEY - Tautulli API key
    * TAUTULLI_NOTIFIER_ID - Tautulli notifier ID for the script notification agent

Arguments:
    * --notifier_id [int] - optional, Tautulli notifier ID for the script notification agent (default: env var TAUTULLI_NOTIFIER_ID)
    * --tautulli_url [str] - optional, Tautulli URL, e.g. http://localhost:8181 (default: env var TAUTULLI_URL)
    * --tautulli_api_key [str] - optional, Tautulli API key (default: env var TAUTULLI_API_KEY)
    * --subject [str] - optional, notification subject (default: Tautulli Notification)
    * --body [str] - required, notification body

Usage:
    python tautulli_notify.py --notifier_id 2 --subject "Test subject" --body "Test notification"
'''

import argparse
import os

import dotenv
import requests

# Load environment variables
dotenv.load_dotenv()
TAUTULLI_URL = os.getenv('TAUTULLI_URL')
TAUTULLI_API_KEY = os.getenv('TAUTULLI_API_KEY')
TAUTULLI_NOTIFIER_ID = os.getenv('TAUTULLI_NOTIFIER_ID')

def notify(subject, body, api_key=TAUTULLI_API_KEY, notifier_id=TAUTULLI_NOTIFIER_ID, base_url=TAUTULLI_URL):
    # Throw an error if the variables are not set
    if not base_url or not api_key or not notifier_id:
        raise Exception('Tautulli URL, API key, and notifier ID are required')

    params = {
        "apikey": api_key,
        "cmd": "notify",
        "notifier_id": notifier_id,
        "subject": subject,
        "body": body
    }

    r = requests.get(base_url.rstrip('/') + '/api/v2', params=params)
    r.raise_for_status()

    return r.json()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--notifier_id', type=int, required=False, default=TAUTULLI_NOTIFIER_ID)
    parser.add_argument('--tautulli_url', type=str, required=False, default=TAUTULLI_URL)
    parser.add_argument('--tautulli_api_key', type=str, required=False, default=TAUTULLI_API_KEY)
    parser.add_argument('--subject', type=str, required=False, default='Tautulli Notification')
    parser.add_argument('--body', type=str, required=True)
    opts = parser.parse_args()

    TAUTULLI_NOTIFIER_ID = opts.notifier_id
    TAUTULLI_URL = opts.tautulli_url
    TAUTULLI_API_KEY = opts.tautulli_api_key

    notify(opts.subject, opts.body, TAUTULLI_API_KEY, TAUTULLI_NOTIFIER_ID, TAUTULLI_URL)
