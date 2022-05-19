# -*- coding: utf-8 -*-

"""
Copyright (c) 2019 Valentin B.
A simple music bot written in discord.py using youtube-dl.
Though it's a simple example, music bots are complex and require much time and knowledge until they work perfectly.
Use this as an example or a base for your own bot and extend it as you want. If there are any bugs, please let me know.
Requirements:
Python 3.5+
pip install -U discord.py pynacl youtube-dl
You also need FFmpeg in your PATH environment variable or the FFmpeg.exe binary in your bot's directory on Windows.
"""

import logging

import nextcord
import youtube_dl
from nextcord.ext import commands
from dotenv import load_dotenv
import setproctitle
import os
from music import Music
import coloredlogs

# Set logging
coloredlogs.install()
log = logging.getLogger(__name__)
log.setLevel("INFO")
logging.info("Set up logs")

# Set workdir
path = os.path.dirname(os.path.abspath(__file__))
working_dir = os.path.dirname(path)
os.chdir(working_dir)

# Dotenv
load_dotenv("env/.env")
token = os.getenv("DISCORD_TOKEN")
prefix = os.getenv("PREFIX")


# Process name
setproctitle.setproctitle("musicbot")

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ""


bot = commands.Bot(prefix, description="Yet another music bot.")
bot.add_cog(Music(bot))
bot.status = nextcord.Status.online
bot.activity = nextcord.Activity(
    name="Cool music", type=nextcord.ActivityType.listening
)


@bot.event
async def on_command_error(context: commands.Context, error: commands.CommandError):
    if (
        isinstance(error, commands.CommandNotFound)
        and "/" not in context.message.content
    ):
        msg = await context.send(
            "Error: Command not found use `-help` to see the available commands"
        )

        await msg.delete(delay=5)


@bot.event
async def on_ready():
    log.info("Logged in as: {}".format(bot.user.name))


bot.run(str(token))
