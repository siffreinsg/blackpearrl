# Quotas Notifier

This script sends a notification via Tautulli when the disk usage or traffic usage exceeds a certain threshold.

## Configuration

First, make sure the tautulli_notify script is installed and working. Refer to the corresponding [README](../tautulli_notify/README.md) for more information.

The script requires the following environment variables to be set:
  - `DISK_USAGE_THRESHOLD_GB` (default=5000): The disk usage threshold in GB.
  - `TRAFFIC_USAGE_THRESHOLD_PERCENT` (default=80): The traffic usage threshold in percent.

## Systemd service

Install the systemd service file to run the script periodically.

```bash
cd ~/.config/systemd/user
ln -s ~/blackpearrl/scripts/quotas_notifier/quotas_notifier.service
ln -s ~/blackpearrl/scripts/quotas_notifier/quotas_notifier.timer
systemctl --user daemon-reload
systemctl --user enable quotas_notifier.service
systemctl --user enable quotas_notifier.timer
```

Edit the `OnCalendar` field in the timer file to set the desired interval or time of day.
Execution every 12 hours or 24 hours is recommended.
Avoid setting the same time for all services to avoid overloading the system.
