# qBit Manage

Make sure to install the requirements.

## Installation
### Using pipenv

```bash
cd ~/blackpearrl/qbit_manage
pipenv install -r qbit_manage/requirements.txt
```

## Configuration

Edit the `config.yaml` file in the `~/blackpearrl/qbit_manage` directory.
No environment variables are required for this tool.

Update the host and port for qBittorrent Web UI.

To authenticate with qBittorrent, you will need to add your username and password to the `config.yaml` file.
Alternatively, you may configure qBittorrent Web UI to bypass authentication for the IP address the script is running from.

## Systemd service

Install the systemd service file.

```bash
cd ~/.config/systemd/user
ln -s ~/blackpearrl/qbit_manage/qbit_manage.service qbit_manage.service
systemctl --user daemon-reload
systemctl --user enable --now qbit_manage
```

## Systemd timer

```bash
cd ~/.config/systemd/user
ln -s ~/blackpearrl/qbit_manage/qbit_manage.timer qbit_manage.timer
systemctl --user daemon-reload
systemctl --user enable --now qbit_manage.timer
```

Verify the timer is running.

```bash
systemctl --user list-timers
```
