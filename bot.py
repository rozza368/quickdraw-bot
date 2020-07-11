# Use discord.py 1.3.3
import discord
from discord.ext import commands
from discord import Game

import re
import data
from bot_token import TOKEN




user_data = data.UserData()

bot = commands.Bot(
        command_prefix=".",
        case_insensitive=True,
        description="Holds data for Quick Draw! players.",
        self_bot=False,
        owner_id=387909176921292801
    )


def get_id_from_mention(mention):
    # remove all non-digit characters
    return int(re.sub(r"\D", "", mention))



@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command(name="inventory", aliases=["inv"])
async def inventory(ctx, usr=None):
    if usr:
        usr = get_id_from_mention(usr)
    else:
        usr = ctx.message.author.id
    
    msg = f"{bot.get_user(usr)}'s inventory:\n{user_data.get_inv(usr)}"
    await ctx.send(msg)


@bot.command(name="logout", hidden=True)
async def logout(ctx):
    if await bot.is_owner(ctx.message.author):
        user_data.save()
        await bot.logout()


@bot.event
async def on_message(message):

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    user = message.author.id
    if message.author == bot.user:
        return

    if not user_data.is_usr(user):
        user_data.init_usr(user)

    await bot.process_commands(message)


@bot.event
async def on_ready():
    print("Successfully logged in")
    print(f"ID: {bot.user.id}\nUsername: {bot.user.name}")
    activity = discord.Activity(name='.help', type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)
    


if __name__ == "__main__":
    print("Starting...")
    bot.run(TOKEN)

