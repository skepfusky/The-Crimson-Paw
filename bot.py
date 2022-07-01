import disnake
import os
import argparse
from colorama import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class CrimsonPaw(disnake.Client):
      async def on_ready(self):
        print(f"Logged on as {self.user}")
        
      async def on_message(self, message):
          print(f"Message from {message.author}: \"{message.content}\"")

client = CrimsonPaw().run(os.getenv("TOKEN"))