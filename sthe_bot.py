# import packages
import asyncio
import json
import os
import sys
import discord
from discord.ext import commands
from discord.ext.commands import Bot

"""
Check for bot_config.json file and makes sure it has been filled out
"""
if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/bot_config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/bot_config.json") as file:
        config = json.load(file)

        if config["token"] == "BOT_TOKEN_HERE":
            sys.exit("'config.json' not found! Please add it and try again.")

"""
Create a bot variable to access the config file in cogs so that you don't need to import it every time.

The config is available using the following code:
- sthe_bot.config       # In this file
- self.sthe_bot.config  # In cogs
"""
sthe_bot        = Bot(command_prefix=commands.when_mentioned_or(config["prefix"]), intents=discord.Intents.all())
sthe_bot.config = config

"""
Bot Startup Routine
- Sets the bot's status to status_game
- Sends a message (if channel_id is set in config file)
"""
startup_status  = "Row, Row, Fight the Power"
startup_message = "Hello, bot is alive"

@sthe_bot.event
async def on_ready():
    print("Hello, bot is alive")
    if isinstance(config["channel_id"], int):
        channel = sthe_bot.get_channel(config["channel_id"])
        await channel.send(startup_message)

    await sthe_bot.change_presence(activity=discord.Game(startup_status))

"""
Load bot cogs within the cogs folder
"""
async def load_cogs():
    for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            print("Loading " + extension + ".py")
            try:
                await sthe_bot.load_extension(f"cogs.{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"

asyncio.run(load_cogs())
sthe_bot.run(config["token"])