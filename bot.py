"""
The Crimson Paw - A Moderation Bot for The Bad Guy's Server

By Kerby Keith Aquino <skepfoosky15@gmail.com>
"""
import disnake
import os
from disnake.ext import commands, tasks
from colorama import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = commands.Bot(command_prefix="d!", intents=disnake.Intents.all(), sync_commands=True)

@client.slash_command(description="Ping the bot for testing purposes")
async def ping(inter):
    await inter.response.send_message("Bing bongs")

@client.slash_command(description="Another embed test command")
async def yeet(ctx):
    embed = disnake.Embed(title="Pong!", description="Bing bongs", color=0x00ff00)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print(f"{Fore.GREEN}[!]{Fore.RESET} Bot is ready! Logged in as {client.user}")
    await client.change_presence(activity=disnake.Game(name="as the Governor"))

client.run(os.getenv("TOKEN"))