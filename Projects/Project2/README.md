# Discord API

## Setup

# Getting an API

In order to get an API, you must have an account on the [Discord development portal](https://discord.com/developers/applications).

Select "New Application", enter name

Go over to the left menu, select Bot

Click "Add Bot", Select "Yes, do it"

Under Token, click "Copy"

In the same directory as the bot.py file, create an new file named .env

This file stores all the enviromental variables to be used in the bot file

Within the .env file insert this line: "DISCORD_TOKEN=your-bot-token"
also add "DISCORD_GUILD={your-server-name}"

If the bot.py does not exist, download [Discord Bot](https://realpython.com/how-to-make-a-discord-bot-python/)

# Dependencies
You would need to install two python packages

1. Discord
2. dotenv

Install them by opening an terminal and typing command
"pip3 install -U python-dotenv"
"pip3 install discord.py"




