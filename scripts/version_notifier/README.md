# Version Notifier

This script is used to notify the user when a new version of a software is available.
It uses the GitHub API to get the latest release of a repository and compares it to the latest version seen by the script.

## Configuration

First, make sure the tautulli_notify script is installed and working. Refer to the corresponding [README](../tautulli_notify/README.md) for more information.

Run the script for the first time to generate the configuration file or copy the services.yaml file to the configuration directory `$APP_DATA_PATH/version_notifier`.

For each software you want to track, add a new section in the configuration file.

```yaml
- label: plex   # Unique identifier for the software
  display_name: Plex    # Display name for the software used in the notification message
  repo: linuxserver/docker-plex  # GitHub repository in the format owner/repo
  target_commitish: master  # Branch or tag to track, usually main or master
```

## Systemd service

Install the systemd service file to run the script periodically.

```bash
cd ~/.config/systemd/user
ln -s ~/blackpearrl/scripts/version_notifier/version_notifier.service
ln -s ~/blackpearrl/scripts/version_notifier/version_notifier.timer
systemctl --user daemon-reload
systemctl --user enable version_notifier.service
systemctl --user enable version_notifier.timer
```

Edit the `OnCalendar` field in the timer file to set the desired interval or time of day.
Execution every 12 hours or 24 hours is recommended to avoid hitting the GitHub API rate limit.
Avoid setting the same time to avoid overlapping with other services.
