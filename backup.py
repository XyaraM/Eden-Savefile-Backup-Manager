from gzip import GzipFile
from shutil import which
from tarfile import *
import tarfile
import os
import shutil
from pathlib import Path
from datetime import datetime

edenPath = ""
whichOs = ""
date = ""

def getDate():
    return datetime.today().strftime('%Y-%m-%d_%H:%M')
date = getDate()

def checkAndCreateDir():
    if not os.path.exists(edenPath + "backups"):
        os.mkdir(edenPath + "backups")

def defineValues():
    if os.name == "posix":
        whichOs = "linuxbsd"
    if whichOs == "linuxbsd":
        edenPath = str(Path.home()) + "/.local/share/eden/"
    else:
        print("Warning: WINDOWS AND MAC ARE NOT IMPLEMENTED YET!!!")
    return edenPath, whichOs
edenPath, whichOs = defineValues()
checkAndCreateDir()

def listBackups():
    print(" ")
    for i in os.listdir(edenPath + "backups"):
        print(i)

def howManyAreThere():
    quantity: int
    if len(os.listdir(edenPath + "backups")) == 0:
        quantity = 0
        return quantity
    else:
        quantity = len(os.listdir(edenPath + "backups/"))
        return quantity

def backupSavefiles():
    fileName = str(howManyAreThere()) + " - " + date + ".tar.bz2"
    filePath = edenPath + "nand/user/save/"
    if os.path.exists(filePath):
        with tarfile.open(fileName, "w:bz2") as tar:
            tar.add(filePath, arcname=os.path.basename(filePath))
            shutil.move(fileName, edenPath + "backups/")
            print("Backup created!: " + fileName)
    else:
        print("There's nothing to back up")

def deleteBackup(backupNumber):
    fileName = str(backupNumber)
    filePath = edenPath + "backups"
    for file in os.listdir(filePath):
        if file.startswith(fileName):
            print("Backup number: " + str(backupNumber) + " deleted!")
            os.remove(path=filePath + "/" + file)

def restoreBackup(backupNumber):
    fileName = str(backupNumber)
    filePath = edenPath + "backups"
    rmPath = edenPath + "nand/user/save/"
    extractPath = edenPath + "nand/user/save/"
    print("\nThe current savefiles are gonna be backed up!\n")
    backupSavefiles()
    if os.path.exists(rmPath):
        for i in os.listdir(rmPath):
            shutil.rmtree(rmPath + i)
    for file in os.listdir(filePath):
        if file.startswith(str(backupNumber)):
            with tarfile.open(filePath + "/" + str(file), "r") as tar:
                tar.extractall(path=extractPath)
                print("Backup restored!")
