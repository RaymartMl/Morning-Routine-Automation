import os
import subprocess
import webbrowser

from pyfiglet import Figlet
from yachalk import chalk

# Helper Functions

def send_notification_on_linux(message):
    subprocess.Popen(["notify-send", message])
    return

def continue_day():
    input(chalk.cyan("Press too continue"))
    print()

def step(message, browser_open=None, os_run=None):
    print(chalk.blue.bold(message))

    if browser_open:
        webbrowser.open(browser_open)
    
    if os_run:
        os.system(os_run)

    continue_day()


# Start
def main():
    figlet = Figlet(font="standard")
    print(chalk.green.bold(figlet.renderText("Start the day")))

    # Timer
    step("Turn on day timer", "https://www.google.com/search?q=3+hours+timer&oq=3+hours+timer&aqs=chrome..69i57.4988j0j1&sourceid=chrome&ie=UTF-8")

    # Music
    step("Turn on white noise", "https://www.youtube.com/watch?v=nMfPqeZjc2c")

    # Notejoy
    step("Create a new note for the day", "https://notejoy.com/")

    # Check slack / email / social
    send_notification_on_linux("Don't get down to the rabbit hole :) ")

    step("Check your Slack", "https://app.slack.com/client/T0U4XB6FJ/D02HC0UB1L5")
    step("Check gmail", "https://mail.google.com/mail/u/0/")
    step("Check Messenger", "https://www.messenger.com/")
    step("Check Facebook", "https://www.facebook.com/")

    # Arrange 
    step("Go back to note joy and arrange your task of the day", "https://notejoy.com/")

    # Vscode
    step("Opening vscode", os_run="qdbus org.kde.KWin /KWin nextDesktop && code")

    print(chalk.green.bold("Be grateful, no negative thoughts and have a great day!"))



if __name__=="__main__":
    main()
