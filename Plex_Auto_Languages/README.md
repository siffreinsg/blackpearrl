# Plex Auto Languages

Make sure to install the requirements.

## Installation
### Using pipenv

```
cd blackpearrl/Plex_Auto_Languages
pipenv install -r Plex_Auto_Languages/requirements.txt
```

## Configuration

Edit the `config.yaml` file in the `~/blackpearrl/Plex_Auto_Languages` directory.

Set the `PLEX_URL` and `PLEX_TOKEN` environment variables in the `~/blackpearrl/.env` file.

## Usage

### Systemd

Install the systemd service file.

```bash
cd ~/.config/systemd/user
ln -s ~/blackpearrl/Plex_Auto_Languages/Plex_Auto_Languages.service Plex_Auto_Languages.service
systemctl --user daemon-reload
systemctl --user enable --now Plex_Auto_Languages
```
