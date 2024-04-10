#!/bin/sh
echo "Running \"python3 $@\" command in venv..."
exec pipenv run python3 "$@"
