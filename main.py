from dotenv import load_dotenv
from pathlib import Path
import random
import os
import discord
import requests
import json
import pyjokes

client = discord.Client()

sad_words = [
    "sad", 
    "depressed", 
    "unhappy", 
    "angry", 
    "miserable", 
    "depressing", 
    "dead", 
    "die", 
    "bored"
]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!",
  "Think Positive"
]

response = requests.get("https://zenquotes.io/api/random")
json_data = json.loads(response.text)
quote = json_data[0]['q'] + " -" + json_data[0]['a']

f = r"http://api.icndb.com/jokes/random"
data = requests.get(f)
tt = json.loads(data.text)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.startswith
    msg1 = message.channel.send
    if msg('#inspire'):
        await msg1(quote)
    if msg('i am going to heaven'):
        await msg1("You will have peace in heaven")
    if msg('i am going to hell'):
        await msg1("no no change your path to heaven")
    if msg('bye bye bot'):
        await msg1("bye bye whoever said by bye to me")
    if msg('bot u are dumb'):
        await msg1("hell u are!")
    if msg('#joke'):
    	await msg1(tt["value"]["joke"])
    if msg('#jokecode'):
    	await msg1(pyjokes.get_joke())
    if any(word in msg for word in sad_words):
    	await msg1(random.choice(starter_encouragements))

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client.run(os.environ['AUTH_TOKEN'])
