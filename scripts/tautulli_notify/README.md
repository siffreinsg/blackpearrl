# Tautulli Notifier

This script is used to send a notification through Tautulli agents. It is used by other scripts in this project to provide information about the execution of the scripts to the user. Notifications are limited to a subject and a body.

I use the Telegram agent to send messages to my phone. Other agents should work as well, but I have not tested them.

## Configuration

First, make sure the Tautulli server is running and configured with the desired agents. Refer to the [Tautulli wiki](https://github.com/Tautulli/Tautulli/wiki/) for more information.

Set the following environment variables:
* `TAUTULLI_API_KEY`: API key for the Tautulli server
* `TAUTULLI_URL`: URL of the Tautulli server
* `TAUTULLI_NOTIFIER_ID`: ID of the notification agent to use

## Usage

This script may also be used as a standalone script to send notifications to Tautulli. The subject and body of the notification are passed as arguments. You may use it for testing purposes or your own scripts.

Supported arguments are:
* `--subject` (default: `Tautulli Notification`): Subject of the notification
* `--body` (required): Body of the notification
* `--notifier_id` (default: `TAUTULLI_NOTIFIER_ID` env variable): ID of the notification agent to use
* `--tautulli_url` (default: `TAUTULLI_URL` env variable): URL of the Tautulli server
* `--tautulli_api_key` (default: `TAUTULLI_API_KEY` env variable): API key for the Tautulli server

Example:
```bash
python3 tautulli_notify.py \
--subject "Test" \
--body "This is a test notification" \
--notifier_id 1 \
--tautulli_url http://localhost:8181 \
--tautulli_api_key abc123
```
