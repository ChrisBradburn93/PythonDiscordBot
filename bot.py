# bot.py
from logging import exception
import os
from urllib import response
import discord
import random
import json
from dotenv import load_dotenv
from discord.ext import commands
from AdventureFunction import AdventureCall
from NPCFunction import NPCCall
from NPCFunction import Gender,Race


intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', case_insensitive=True)


def select_random_image_path():
    if random.choice(Gender) == "Female" and random.choice(Race) == "Elf":
        Elf_Fem_images = os.path.join(os.getcwd(), "\\Users\\Gamer\\Repos\\GitHubCloned\\PythonDiscordBot\\simple_images\\Elf_Female_DND_Portraits")
        return os.path.join(Elf_Fem_images, random.choice(os.listdir(Elf_Fem_images)))

    elif random.choice(Gender) == "Male" and random.choice(Race) == "Elf":
        Elf_Male_images = os.path.join(os.getcwd(), "\\Users\\Gamer\\Repos\\GitHubCloned\\PythonDiscordBot\\simple_images\\Elf_Male_DND_Portraits")
        return os.path.join(Elf_Male_images, random.choice(os.listdir(Elf_Male_images)))

    elif random.choice(Gender) == "Male" and random.choice(Race) == "Dragonborn":
        DB_Male_images = os.path.join(os.getcwd(), "\\Users\\Gamer\\Repos\\GitHubCloned\\PythonDiscordBot\\simple_images\\Dragonborn_Male_portraits")
        return os.path.join(DB_Male_images, random.choice(os.listdir(DB_Male_images)))

    elif random.choice(Gender) == "Female" and random.choice(Race) == "Dragonborn":
        DB_Female_images = os.path.join(os.getcwd(), "\\Users\\Gamer\\Repos\\GitHubCloned\\PythonDiscordBot\\simple_images\\Dragonborn_Female_portraits")
        return os.path.join(DB_Female_images, random.choice(os.listdir(DB_Female_images)))

    else:  
        Error_Image = os.path.join(os.getcwd(), "\\Users\\Gamer\\Repos\\GitHubCloned\\PythonDiscordBot\\simple_images\\errorcache")
        return os.path.join(Error_Image, random.choice(os.listdir(Error_Image)))


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

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
    f'Hi {member.name}, welcome to the server. Play nice or you''ll get got!'
    )

@bot.command(name='AV', help='Generates an adventure hook for use in D&D')
async def Adventure(ctx):
        response = AdventureCall()
        await ctx.send(response)

@bot.command(name='NPC', help='Generates a NPC for use in D&D')
async def NPC(ctx):
        response = NPCCall()
        await ctx.send(response)
        await ctx.send(file=discord.File(select_random_image_path()))
        

@bot.command(name='Dice', help='Rolls dice. Duh. It is case sensitive."')
async def roll(ctx, sides, amount):
  try:
    sides = int(sides.split("D")[1])
    rolls_list = []
    for number in range(int(amount)):
       # 1 is the minimum number the dice can have
       rolls_list.append(random.randint(1, sides))
    rolls = ", ".join(str(number) for number in rolls_list)
    await ctx.send("Your dice rolls were: " + rolls)
  except Exception as e:
    print(e)
    await ctx.send("Incorrect format for sides of dice (try something like \"!Dice D6 1 (Case sensitive for D)\").")

bot.run(TOKEN)