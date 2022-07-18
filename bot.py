"""
The Crimson Paw - A Moderation Bot for The Bad Guy's Server

By Kerby Keith Aquino <skepfoosky15@gmail.com>
"""
import disnake
import os
from dotenv import load_dotenv
from disnake.ext import commands, tasks
from colorama import *

load_dotenv()

client = commands.Bot(intents=disnake.Intents.all(), sync_commands=True)

# Main execution
@client.slash_command(description="Ping the bot for testing purposes")
async def ping(inter):
    await inter.response.send_message("Bing bongs")

@client.slash_command(description="Another embed test command")
async def help(ctx):
    embed = disnake.Embed(title="Pong!", description="mark is bae", color=0x00ff00)
    embed.set_image(url="https://media.giphy.com/media/ycTVuMYzKu4vHg1OLG/giphy.gif")
    await ctx.send(embed=embed)

@client.slash_command(description="Get user information")
async def user(ctx, user: str):
    if user == "":
        user = ctx.author.name

    user = await client.get_user(user)
    embed = disnake.Embed(title=f"{user.name}#{user.discriminator}", color=0x00ff00)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="ID", value=user.id, inline=False)
    embed.add_field(name="Status", value=user.status, inline=False)
    embed.add_field(name="Created At", value=user.created_at, inline=False)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print(f"{Fore.GREEN}[!]{Fore.RESET} Bot is ready! Logged in as {client.user}")
    await client.change_presence(activity=disnake.Game(name="as the Governor"))

client.run(os.getenv("TOKEN"))