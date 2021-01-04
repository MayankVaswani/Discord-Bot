from dotenv import load_dotenv
from pathlib import Path
import os
import discord
import requests
import json


client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    global quote
    quote = json_data[0]['q'] + " -" + json_data[0]['a']


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        await message.channel.send(quote)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client.run(os.environ['AUTH_TOKEN'])
