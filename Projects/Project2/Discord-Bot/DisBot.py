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

    cool_facts = [
        'The first oranges weren’t orange, but green',
        'McDonald’s once made bubblegum-flavored broccoli',
        'Q is the only letter that does not appear in any U.S. state name',
	    'Johnny Chapman (Appleseed) planted apple trees, but apples were much bitter, only to be used in cider',
	    'Kleenex tissues were originally intended for gas masks'
    ]
    roll_dice = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6'
    ]
	#https://www.rd.com/list/interesting-facts/
    if message.content == 'learn!':
        response = random.choice(cool_facts)
        await message.channel.send(response)
    
    if message.content == 'rollthedice!':
        await message.channel.send('Rolling Dice')
        response = random.choice(roll_dice)
        await message.channel.send('Still rolling')
        response = random.choice(roll_dice)
        await message.channel.send('Even more rolling')
        response = random.choice(roll_dice)
        await message.channel.send('You rolled a ' + response)

client.run(TOKEN)
