# Use discord.py 1.3.3
import discord
from discord.ext import commands
from discord import Game

import data
from token import TOKEN


class Bot:
    bot = commands.Bot(
            command_prefix = ".",
            case_insensitive = True,
            description = "Holds data for Quick Draw! players.",
            self_bot = False
        )
    

    def __init__(self):
        pass
    

    @bot.command(name="hello")
    async def hello(self, ctx):
        await ctx.send("Hi!")


    @bot.event
    async def on_ready(self):
        print("Successfully logged in")
        activity = discord.Activity(name='Quick Draw!', type=discord.ActivityType.playing)
        await self.bot.change_presence(activity=activity)
    

    def run(self, token):
        self.bot.run(token)


if __name__ == "__main__":
    bot = Bot()
    bot.run(TOKEN)