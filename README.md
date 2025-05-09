# Blackpearrl
Collection of scripts and configs for my Ultra.cc seedbox

Tools from the community are included in this repo as git submodules. For each tool, I have included my own configuration files and scripts. This repo is intended to be a one-stop shop for all the tools I use on my seedbox.
I do not take credit for any of the tools included in this repo. Please refer to the original authors for support and questions.

My own tools are included in the `scripts` directory and are licensed under the GNU General Public License v3.0.

All scripts and systemd configs are intended to be used on an Ultra.cc seedbox. While I try to make them as generic as possible, they may not be suitable for other hosts.

# Usage

## Clone the repo

All scripts and configs are intended to be used from the `$HOME/blackpearrl` directory and rely on submodules. You will have to update scripts and systemd service files if you clone the repo to a different directory.
Clone the repo in the home directory with the following command:

```bash
cd $HOME
git clone https://github.com/siffreinsg/blackpearrl
cd blackpearrl
git submodule update --init --recursive --filter=tree:0 --single-branch
```

## Pipenv

Most tools use pipenv to manage dependencies. By default, this repository assumes that pipenv is installed in `~/.local/bin/pipenv`.

If pipenv is installed elsewhere, you may need to modify systemd service files and scripts to reflect the correct path.

Install pipenv for the current user with the following command:

```bash
pip install --user pipenv
```

## Set environment variables

Create a file called `.env` in the `~/blackpearrl` directory and add the necesssary environment variables.
Variables are described in the documentation for each tool.

You may load the environment variables with the following command for the current shell session:

```bash
set -o allexport
source .env set
set +o allexport
```

## Use Black Pearl .profile
A `.profile` file is included. This file provides utility functions and aliases for the shell as well as setting up environment variables. You may source this file in your shell profile to have the environment variables available in all shell sessions.

Add the following line to your shell profile:

```bash
source ~/blackpearrl/.profile
```

Note that the `.profile` file is intended for bash and zsh. If you use a different shell, you may need to modify the file to work with your shell.
Please review the file before sourcing it to ensure it is compatible with your shell and environment.
