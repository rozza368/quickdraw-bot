# Use discord.py 1.3.3
import discord
from discord.ext import commands
from discord import Game
import data
from bot_token import TOKEN




bot = commands.Bot(
        command_prefix = ".",
        case_insensitive = True,
        description = "Holds data for Quick Draw! players.",
        self_bot = False
    )


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hi!")


@bot.event
async def on_ready():
    print("Successfully logged in")
    print(f"ID: {bot.user.id}\nUsername: {bot.user.name}")
    activity = discord.Activity(name='Quick Draw!', type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)


if __name__ == "__main__":
    bot.run(TOKEN)

