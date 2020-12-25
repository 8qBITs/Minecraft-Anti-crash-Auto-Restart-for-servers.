import threading, json, os, time
from os import system
from subprocess import getoutput
from time import sleep

print("Umbra.Solutions > Server Auto Restart")

# Load config file

with open('config.json') as config_file:
    data = json.load(config_file)

# Settings

_NAME = data['name']
_RESTARTS = data['restarts']
_COMMAND = data['command']

def checkSession():
    # Check if screen session is open.
    if _NAME in os.popen("screen -ls").read():
        return True
    else:
        return False

def startSession():
    # Start the server in a screen session.
    if not checkSession():
        os.chdir(_PATH)
        os.popen("screen -dmS " + _NAME)
        # Send command to start server
        os.popen("screen -S " + _NAME + " -X stuff '" + _COMMAND + "^M'")

def stopSession():
    # Stop the server session.
    if checkSession():
        os.popen("screen -X -S " + _NAME + " quit")

def autoRestart():
    # Restart server on chosen timestamps.
    while True:
        timestamp = time.strftime('%H:%M')
        if timestamp in _RESTARTS:
            # Restart the session
            stopSession()
            sleep(10)
            startSession()
        else:
            sleep(1)

autoRestart()

