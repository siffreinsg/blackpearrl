'''
Description:  Send a Tautulli notification when disk usage exceeds a threshold. Only compatible with Unix-like systems with du command available.
Author:       Siffrein SIGY <hello@siffreinsigy.com> (GitHub: siffreinsg)
Requires:     subprocess, dotenv, tautulli_notify

Tautulli script trigger:
   * Notify on recently added

Environment variables:
    * DISK_USAGE_PATH - Path to check disk usage for, default is home directory
    * DISK_USAGE_THRESHOLD_GB - Disk usage threshold in GB, default is 2500 GB

Usage:
    python notify_disk_usage.py
'''

import os
import sys
from pathlib import Path

import dotenv

# Add the parent directory to the path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Import the notify function from tautulli_notify
from tautulli_notify.tautulli_notify import notify

# Load environment variables
dotenv.load_dotenv()
DISK_USAGE_PATH = os.getenv('DISK_USAGE_PATH', os.path.expanduser('~') + '/')
DISK_USAGE_THRESHOLD_GB = int(os.getenv('DISK_USAGE_THRESHOLD_GB', 2500))


def get_folder_size(folder):
    """Get the size of a folder in bytes.

    Args:
        folder (str): Path to the folder to check disk usage for.

    Returns:
        int: Size of the folder in bytes.
    """
    return sum(file.stat().st_size for file in Path(folder).rglob('*') if file.is_file())


def notify_usage(path: str = DISK_USAGE_PATH, threshold_gb: int = DISK_USAGE_THRESHOLD_GB):
    """Check disk usage for a path and notify if it exceeds a threshold.

    Args:
        path (str, optional): Path to check disk usage for. Defaults to DISK_USAGE_PATH.
        threshold_gb (int, optional): Disk usage threshold in GB. Defaults to DISK_USAGE_THRESHOLD_GB.

    Returns:
        tuple: A tuple with a boolean indicating if disk usage exceeds the threshold and the disk usage in GB.
    """
    disk_usage_b = get_folder_size(path)
    disk_usage_gb = round(disk_usage_b / 1_000_000_000, 2)
    exceeding = disk_usage_gb > threshold_gb

    if exceeding:
        notify(
            '<b>Disk Usage Alert</b>',
            f"Path <code>{DISK_USAGE_PATH}</code> disk usage is <b>{disk_usage_gb} GB</b> exceeding threshold of <b>{DISK_USAGE_THRESHOLD_GB} GB</b>."
        )

    return exceeding, disk_usage_gb

if __name__ == '__main__':
    print(f"Checking disk usage for path {DISK_USAGE_PATH}...")

    exceeding, disk_usage_gb = notify_usage()

    if exceeding:
        print(f"Disk usage for path {DISK_USAGE_PATH} is about {disk_usage_gb} GB, exceeding threshold of {DISK_USAGE_THRESHOLD_GB} GB.")
    else:
        print(f"Disk usage for path {DISK_USAGE_PATH} is about {disk_usage_gb} GB, under threshold of {DISK_USAGE_THRESHOLD_GB} GB.")
