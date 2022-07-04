"""
The Crimson Paw Moderation Bot

Written in Python by Kerby Keith Aquino<skepfoosky15@gmail.com>
"""
import disnake
import os
import argparse
from colorama import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class CrimsonPaw(disnake.Client):
    async def on_ready(self):
        print(f"{Fore.LIGHTGREEN_EX}Client is ready! Logged on as {self.user}.{Style.RESET_ALL}")

    async def on_message(self, message):
        print(f"Message from {message.author}: \"{message.content}\"")


client = CrimsonPaw().run(os.getenv("TOKEN"))
