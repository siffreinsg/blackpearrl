# Recyclarr

Ultra.cc provide an unofficial installer for recyclarr.
Docs available here: [Recyclarr on docs.ultra.cc](https://docs.ultra.cc/books/unofficial-application-installers/page/recyclarr)

Please refer to the official recyclarr documentation for more information : [Recyclarr](https://recyclarr.dev)

## Configuration

Using the Ultra.cc installer, recyclarr configuration is located at `~/.apps/recyclarr`.

Assuming this repository is cloned to `~/blackpearrl`, the configuration can be linked to the repository with the following command:

```bash
cd ~/.apps/recyclarr
ln -s ~/blackpearrl/recyclarr/configs configs
```

Create a `secrets.yml` file in the `~/.apps/recyclarr` directory with the following content:

```yaml
sonarr_base_url: https://path.to/sonarr
sonarr_api_key: 0123456789abcdef

radarr_base_url: https://path.to/radarr
radarr_api_key: 0123456789abcdef

radarr2_base_url: https://path.to/radarr2
radarr2_api_key: 0123456789abcdef
```

Now, delete any content in the `~/.apps/recyclarr/recyclarr.yml` file:

```bash
echo "" > ~/.apps/recyclarr/recyclarr.yml
```

## Usage

To start the application in dry mode, run the following command:

```bash
recyclarr sync --preview
```
