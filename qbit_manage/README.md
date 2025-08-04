# qBit Manage

## Installation

Please follow instructions from Ultra.cc to install qbit_manage available in the [documentation](https://docs.ultra.cc/unofficial-application-installers/qbit-manage).

## Configuration

Edit the `config.yaml` file in the `~/blackpearrl/qbit_manage` directory.
Set the `QBT_HOST` environment variable to the IP address or host of the machine running qBittorrent. Set `QBT_USER` and `QBT_PASS` if you are using authentication. Alternatively, you may configure qBittorrent Web UI to bypass authentication for the IP address the script is running from.

## Systemd service

Install the systemd service file.

```bash
cd ~/.config/systemd/user
ln -s ~/blackpearrl/qbit_manage/qbit_manage.service qbit_manage.service
systemctl --user daemon-reload
systemctl --user enable --now qbit_manage
```

## Execution on torrent completion

The script can be run when a torrent completes downloading. To do this, you will need to configure qBittorrent to run a script on torrent completion.

1. Open qBittorrent Web UI.
2. Open the settings.
3. Go to the "Downloads" section.
4. In the "Run external program on torrent completion" field, enter `systemctl --user start qbit_manage`.

## Systemd timer

The script can be run on a schedule using a systemd timer. By default, the script will run every day at 3:05 AM. To change the schedule, edit the `qbit_manage.timer` file.

```bash
cd ~/.config/systemd/user
ln -s ~/blackpearrl/qbit_manage/qbit_manage.timer qbit_manage.timer
systemctl --user daemon-reload
systemctl --user enable --now qbit_manage.timer
```

Verify the timer is set up.

```bash
systemctl --user list-timers
```
