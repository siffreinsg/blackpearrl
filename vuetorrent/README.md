# VueTorrent

## Install VueTorrent

```sh
cd ~/.apps
git clone --depth=1 --single-branch --branch=latest-release https://github.com/VueTorrent/VueTorrent.git vuetorrent
```

Point qBitorrent WebUI root folder to ~/.apps/vuetorrent.

## Auto-update

```sh
ln -s ~/blackpearrl/vuetorrent/update-vuetorrent.service ~/.config/systemd/user/update-vuetorrent.service
ln -s ~/blackpearrl/vuetorrent/update-vuetorrent.timer ~/.config/systemd/user/update-vuetorrent.timer
systemctl --user daemon-reload
systemctl --user enable update-vuetorrent.timer
systemctl --user start update-vuetorrent.timer
```
