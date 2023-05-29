import discord
from discord.ext import commands
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)

triggers = [
    "should i",
    "how do i",
    "doesn't work",
    "doesnt work",
]

channel_whitelist = [
    1091806450097082388,
]

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if not message.channel.id in channel_whitelist:
        return

    message_content = message.content.lower()

    for t in triggers:
        if t in message_content:
            await message.reply("hey nerd, chances are you're looking for help. if so then we have a channel for that right here: <#648964758128558103> and you should go there and ask instead of here for fucks sake. imagine not being able to read lmao look at this guy")

with open("config.json", "r", encoding="utf-8") as config:
    config = json.load(config)

bot.run(config["token"])
