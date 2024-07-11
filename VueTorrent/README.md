```sh
cd ~/.apps/nginx/proxy.d # Ultra.cc specific
ln -s ~/blackpearrl/VueTorrent/nginx-backend.conf vuetorrent-backend.conf
# Restart Nginx on Ultra.cc web panel
```

Customize running port in vuetorrent-backend.service and nginx-backend.conf



Install the systemd service file.

```bash
cd ~/.config/systemd/user
ln -s ~/blackpearrl/VueTorrent/vuetorrent-backend.service
systemctl --user daemon-reload
systemctl --user enable --now vuetorrent-backend
```
