import os
import subprocess
import time
import webbrowser
from datetime import datetime
from email import message

# Helper Functions

def sendNotificationOnLinux(message):
    subprocess.Popen(["notify-send", message])
    return

def continueDay():
    cont = input("Press too continue")
    print()

# Start

# Timer
print("Turn on day timer")
webbrowser.open("https://www.google.com/search?q=3+hours+timer&oq=3+hours+timer&aqs=chrome..69i57.4988j0j1&sourceid=chrome&ie=UTF-8")
continueDay()

# Music
print("Turn on white noise")
webbrowser.open("https://www.youtube.com/watch?v=nMfPqeZjc2c")
continueDay()

# Notejoy
print("Create a new note for the day")
webbrowser.open("https://notejoy.com/")
continueDay()

# Check slack / email / social
sendNotificationOnLinux("Check slack / email / social (Don't get down to the rabbit hole :) )")

print("Check your Slack")
webbrowser.open("https://app.slack.com/client/T0U4XB6FJ/D02HC0UB1L5")
continueDay()

print("Check gmail")
webbrowser.open("https://mail.google.com/mail/u/0/")
continueDay()

print("Check Messenger")
webbrowser.open("https://www.messenger.com/")
continueDay()

print("Check Facebook")
webbrowser.open("https://www.facebook.com/")
continueDay()

# Arrange 
print("Go back to note joy and arrange your task of the day")
webbrowser.open("https://notejoy.com/")
continueDay()

# Vscode
print("Opening vscode")
os.system("code")
continueDay()

print("Be grateful, no negative thoughts and have a great day!")



