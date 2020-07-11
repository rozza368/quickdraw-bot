# Use discord.py 1.3.3
import discord
from discord.ext import commands
from discord import Game

import os

import data
from bot_token import TOKEN



bot = commands.Bot(
        command_prefix = ".",
        case_insensitive = True,
        description = "Holds data for Quick Draw! players.",
        self_bot = False
    )


def __init__(self):
    # ensure data file exists
    if not os.path.isfile("data.json"):
        with open("data.json", "w") as data_file:
            data_file.write("{}")


@bot.command(name="hello")
async def hello(self, ctx):
    await ctx.send("Hi!")


@bot.event
async def on_ready(self):
    print("Successfully logged in")
    print(f"ID: {bot.user.id}\nUsername: {bot.user.name}")
    activity = discord.Activity(name='Quick Draw!', type=discord.ActivityType.playing)
    await self.bot.change_presence(activity=activity)
    


if __name__ == "__main__":
    bot.run(TOKEN)
