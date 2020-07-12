import os

if not os.path.isfile("bot_token.py"):
    with open("bot_token.py", "w") as f:
        f.write("# Paste your bot token in between the quotes.\nTOKEN = ''")
    print("No token file found, so one has been created. Please add your bot token to 'bot_token.py'")
    exit()

# Use discord.py 1.3.3
import discord
from discord.ext import commands
from discord import Game
import asyncio

import re
from bot_token import TOKEN
import data

user_data = data.UserData()


           # Blocky            # rozza             # Derpy
ownerid = [346107577970458634, 387909176921292801, 553154552908611584]
# used to be is_admin, changed to reduce confusion
def is_owner(authorid):
    return authorid in ownerid

def is_admin(usr, guild):
    admin_role = discord.utils.find(lambda r: r.name == 'Server Admin', guild.roles)
    return admin_role in usr.roles

def get_id_from_mention(mention):
    # remove all non-digit characters
    return int(re.sub(r"\D", "", mention))

bot = commands.Bot(
    command_prefix=".",
    case_insensitive=True,
    description="Holds data for Quick Draw! players.",
    self_bot=False
)

cogs = [
    "cogs.characters"
]
cogs_loaded = False


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hi!")


# Rory now we can both do it
@bot.command(name="logout", hidden=True)
async def logout(ctx):
    author = ctx.message.author
    authorid = ctx.message.author.id
    msg = f"{author.mention}, Logging out"
    msg1 = f"{author.mention}, You do not have permission to use this command."
    if is_owner(authorid):
        user_data.save()
        await ctx.send(msg)
        await bot.logout()
    else:
        await ctx.send(msg1)


@bot.command(name="reload")
async def reload(ctx):
    if is_owner(ctx.message.author.id):
        print("Reloading cogs.")
        for cog in cogs:
            bot.unload_extension(cog)
            bot.load_extension(cog)
        await ctx.send("Reloaded cogs.")
    else:
        await ctx.send("Insufficient permissions.")


@bot.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if message.author == bot.user:
        return

    # user = message.author.id

    await bot.process_commands(message)


@bot.event
async def on_ready():
    global cogs_loaded
    if not cogs_loaded:
        for cog in cogs:
            bot.load_extension(cog)
        cogs_loaded = True
    print("Successfully logged in")
    print(f"ID: {bot.user.id}\nUsername: {bot.user.name}")
    activity = discord.Activity(name='for .help', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)


if __name__ == "__main__":
    print("Starting...")
    bot.run(TOKEN)
