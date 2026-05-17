import subprocess
import sys

import backup

isProgramActive: bool = True
isFirstEntry: bool = False
arguments = sys.argv[1:]

usage_message = """
Usage: start.py [OPTIONS] number

OPTIONS:
    interact    - Enables the interactive mode
    list        - List your backups
    create      - Create a new backup
    delete      - Delete your backup
    restore     - Restore your backup
"""


def detectArgument(arg: str):
    match arg:
        case "create":
            backup.backupSavefiles(False)
        case "list":
            backup.listBackups()
        case "delete":
            if len(arguments) > 1 and arguments[1].isdigit():
                backup.deleteBackup(arguments[1])
            else:
                print("Select the number of the backup.")
        case "restore":
            if len(arguments) > 1 and arguments[1].isdigit():
                backup.restoreBackup(arguments[1])
            else:
                print("Select the number of the backup.")
        case "interact":
            subprocess.run("venv/bin/python3 interactive.py", shell=True)


if len(arguments) == 0:
    print(usage_message)
else:
    try:
        detectArgument(arguments[0])
    except IndexError:
        pass
