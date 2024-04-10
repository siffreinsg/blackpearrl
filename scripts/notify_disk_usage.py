'''
Description:  Send a Tautulli notification when disk usage exceeds a threshold. Only compatible with Unix-like systems with du command available.
Author:       Siffrein SIGY <hello@siffreinsigy.com> (GitHub: siffreinsg)
Requires:     subprocess, dotenv, tautulli_notify

Tautulli script trigger:
   * Notify on recently added

Environment variables:
    * DISK_USAGE_PATH - Path to check disk usage for, default is home directory
    * DISK_USAGE_THRESHOLD - Disk usage threshold in GB, default is 2500 GB

Usage:
    python notify_disk_usage.py
'''

import os
from pathlib import Path

import dotenv
from tautulli_notify.tautulli_notify import notify


def get_folder_size(folder):
    """Get the size of a folder in bytes.

    Args:
        folder (str): Path to the folder to check disk usage for.

    Returns:
        int: Size of the folder in bytes.
    """
    return sum(file.stat().st_size for file in Path(folder).rglob('*') if file.is_file())


if __name__ == '__main__':
    # Load environment variables
    dotenv.load_dotenv()
    DISK_USAGE_PATH = os.getenv('DISK_USAGE_PATH', os.path.expanduser('~') + '/')
    DISK_USAGE_THRESHOLD_GB = int(os.getenv('DISK_USAGE_THRESHOLD_GB', 2500))

    print(f"Checking disk usage for path {DISK_USAGE_PATH}...")

    disk_usage_b = get_folder_size(DISK_USAGE_PATH)
    disk_usage_gb = round(disk_usage_b / 1_000_000_000, 2)

    if disk_usage_gb <= DISK_USAGE_THRESHOLD_GB:
        print(f"Disk usage for path {DISK_USAGE_PATH} is about {disk_usage_gb} GB, under threshold of {DISK_USAGE_THRESHOLD_GB} GB.")
        exit()

    print(f"Disk usage for path {DISK_USAGE_PATH} is about {disk_usage_gb} GB, exceeding threshold of {DISK_USAGE_THRESHOLD_GB} GB.")
    notify(
        '<b>Disk Usage Alert</b>',
        f"Path <code>{DISK_USAGE_PATH}</code> disk usage is <b>{disk_usage_gb} GB</b> exceeding threshold of <b>{DISK_USAGE_THRESHOLD_GB} GB</b>."
    )
