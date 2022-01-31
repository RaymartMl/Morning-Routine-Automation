from pyfiglet import Figlet
from yachalk import chalk

figlet = Figlet(font="standard")
print(chalk.green.bold(figlet.renderText("Start the day")))
print(chalk.green.bold("Be grateful, no negative thoughts and have a great day!"))
# Compose multiple styles using the chainable API
