import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    odd_quotes = [
        'Who knows what the future will bring',
	'what do you thing will happen now'
    ]

    cool_facts = [
         'The first oranges weren’t orange, but green',
         'McDonald’s once made bubblegum-flavored broccoli',
         'Q is the only letter that does not appear in any U.S. state name',
	 'Johnny Chapman (Appleseed) planted apple trees, but apples were much bitter, only to be used in cider',
	 'Kleenex tissues were originally intended for gas masks'
    ]
	#https://www.rd.com/list/interesting-facts/
    if message.content == 'learn!':
        response = random.choice(cool_facts)
        await message.channel.send(response)
    if message.content == 'future!':
	response = random.choice(odd_quotes)
	await message.channel.send(response)
client.run(TOKEN)
