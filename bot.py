# bot.py
import os
from urllib import response
import discord
import random
import json
from dotenv import load_dotenv
from QHFunction import AdventureCall

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
    f'Hi {member.name}, welcome to the server. Play nice or you''ll get got!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'I want to go on an adventure!':
        response = AdventureCall()
        await message.channel.send(response)


client.run(TOKEN)
