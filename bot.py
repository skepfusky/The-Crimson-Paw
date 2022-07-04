"""
The Crimson Paw Moderation Bot

Written in Python by Kerby Keith Aquino<skepfoosky15@gmail.com>
"""
import disnake
import os
from disnake.ext import commands, tasks
from colorama import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

intents = disnake.Intents.all()
client = commands.Bot(intents=intents, sync_commands=True)

@client.slash_command(description="Ping the bot for testing purposes")
async def ping(inter):
    await inter.response.send_message("Bing bongs")

@client.event
async def on_ready():
    print(f"{Back.GREEN}[!]{Back.RESET} Bot is ready! Logged in as {client.user}")
    # await client.change_presence(activity=disnake.Game(name="testing testing"))

client.run(os.getenv("TOKEN"))