import os
import subprocess
import sys

pyVer = sys.version
path = os.getcwd()


def checkIfVenv():
    if os.path.exists(path + "/venv"):
        return True
    else:
        return False


if pyVer.startswith("3"):
    if checkIfVenv():
        subprocess.run("venv/bin/python3 start.py", shell=True)
    else:
        subprocess.run("python -m venv venv", shell=True)
        subprocess.run("venv/bin/pip install -r requirements.txt", shell=True)
else:
    print("Python 3 is needed")
