#! /usr/bin/env python3

import math
import os
import shutil
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Return True if there isn't enough disk space, otherwise False"""
    du = shutil.disk_usage(disk)
    #Calc % of free space
    percent_free = 100 * du.free / du.total
    #Calc free GB
    gigabytes_free = du.free / 2**30
    print(f"Total size: {math.trunc(du.total/2**30)} GB\nFree Space: {math.floor(percent_free)}% ({math.trunc(gigabytes_free)} GB)")
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False


def check_root_full():
    """Return true if the root partition is full, false otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    if check_reboot():
        print("Pending reboot")
        sys.exit(1)
    else: 
        print("Everything ok.")

    if check_root_full():
        print("Root is full")
        sys.exit(1)
    else: 
        print("Root has space woo")

    sys.exit(0)

main()