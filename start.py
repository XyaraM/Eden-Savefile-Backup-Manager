from shutil import which
import backup

isProgramActive: bool = True
isFirstEntry: bool = False

while isProgramActive:
    if not isFirstEntry:
        print("*_-.EDEN SAVEFILE BACKUP MANAGER.-_*\nType 'help' if you want to display the help message")
        isFirstEntry = True
    entry = input("\nInput: ")

    if entry == "help":
        print("\nListing the backups: list\nCreate a new backup: create\nDelete a backup: delete\nRestore a backup: restore\nExit the program: exit")
    elif entry == "list":
        backup.listBackups()
    elif entry == "create":
        backup.backupSavefiles()
    elif entry == "delete":
        whichBackupToDelete = input("Which backup do you want to delete?: ")
        if whichBackupToDelete.isdigit():
            backup.deleteBackup(int(whichBackupToDelete))
        else:
            print("\nThe input must be a digit!")
    elif entry == "restore":
        whichBackupToRestore = input("Which backup do you want to restore?: ")
        if whichBackupToRestore.isdigit():
            backup.restoreBackup(int(whichBackupToRestore))
        else:
            print("\nThe input must be a digit!")
    elif entry == "exit":
        isProgramActive = False
