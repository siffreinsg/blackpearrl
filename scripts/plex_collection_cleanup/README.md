# Plex Collection Cleanup

This script is used to delete empty collections in Plex.

## Configuration

The script requires the following environment variables to be set: `PLEX_URL`, `PLEX_TOKEN`.
Set these in the `.env` file in the root of the repository.

## Systemd service

Install the systemd service file to run the script periodically.

```bash
cd ~/.config/systemd/user
ln -s ~/blackpearrl/scripts/plex_collection_cleanup/plex_collection_cleanup.service
ln -s ~/blackpearrl/scripts/plex_collection_cleanup/plex_collection_cleanup.timer
systemctl --user daemon-reload
systemctl --user enable plex_collection_cleanup.service
systemctl --user enable plex_collection_cleanup.timer
```

Edit the `OnCalendar` field in the timer file to set the desired interval or time of day.
Execution every 12 hours or 24 hours is recommended.
Avoid setting the same time to avoid overlapping with other services.
