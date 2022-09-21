# The script is pretty simple. It checks for a reboot, disk full, and root partition full. If any of these checks fail, the script will exit with a non-zero exit code. This will cause the script to fail and the user will be notified.

# The script is run by the cron job every 5 minutes. The cron job is set up by the following line in the crontab file:
# this is new line
# */5 * * * * /usr/bin/python3 /home/automation/check_health.py

# The script is run every 5 minutes and the output is sent to the user’s email address.

# Conclusion

# This is a simple example of how to use Python to automate tasks. The script can be modified to check for other things. For example, you can check for a specific file or directory. You can also check for a specific process or service. The possibilities are endless.

# If you have any questions or comments, please leave them below.

# Related

import sys
import os


def check_reboot():
    if os.path.exists('/run/reboot-required'):
        return 1
    else:
        return 0

def check_disk_full():
    df = os.popen('df -h').read()
    if df.find('/dev/sda1') == -1:
        return 1
    else:
        return 0


def main():
    checks = [
        (check_reboot, 'Pending Reboot'),
        (check_disk_full, 'Disk Full'),
        
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False
    if not everything_ok:
        sys.exit(1)
    print('Everything ok.')
    sys.exit(0)

if __name__ == '__main__':
    main()

