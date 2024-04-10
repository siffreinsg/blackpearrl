# Black Pearrl Script Collection

This is a collection of scripts that I have written for my seedbox. Some of them are useful, some of them are not. Some of them are good, some of them are bad. Some of them are ugly, some of them are beautiful. Some of them are fast, some of them are slow. Some of them are big, some of them are small. Some of them are complex, some of them are simple. Some of them are smart, some of them are stupid. Some of them are funny, some of them are boring.

Each script should have a README or a header that explains what it does, how to use it, and what it requires.

Feel free to use these scripts, modify them, and share them as intended by the LICENSE.
If you find a bug, or have a suggestion, please open an issue or a pull request on the GitHub repository with relevant information.

## Installation

I use `pipenv` to manage the dependencies for these scripts. If you don't have `pipenv` installed, you can install it with `pip`:

```bash
pip install pipenv --user
```

### Using pipenv

```bash
cd ~/blackpearrl/scripts
pipenv install
```

## Usage

Each script should have a README or a header that explains how to use it.

To run a script from Tautulli, a `wrapper.sh` script is provided to run scripts in the `pipenv` environment.
Pass the script path as the first argument to the `wrapper.sh` script. Subsequent arguments are passed to the script.

For example, to run the `version_notifier.py` script:
```bash
./wrapper.sh version_notifier/version_notifier.py
```
