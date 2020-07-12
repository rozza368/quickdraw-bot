# Use discord.py 1.3.3
import discord
from discord.ext import commands
from discord import Game
import asyncio

import re
import data
from bot_token import TOKEN
from admin import AdminData

user_data = data.UserData()
admin_data = AdminData()

bot = commands.Bot(
    command_prefix=".",
    case_insensitive=True,
    description="Holds data for Quick Draw! players.",
    self_bot=False
)

def get_id_from_mention(mention):
    # remove all non-digit characters
    return int(re.sub(r"\D", "", mention))

def mention_from_id(id):
    id = "<@" + id + '>'
    return str(id)


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hi!")


# This needs to be fixed
create_order = (
    ("{}, enter the name.", "name"),
    ("{}, enter the age. It must be higher than 20.", "age"),
    ("{}, enter the gender.", "gender"),
    ("{}, enter the county.", "county"),
    ("{}, enter the physical description.", "physical"),
    ("{}, enter the personality description.", "personality"),
    ("{}, enter the special skill. This is optional, so send a dot if you don't want to fill it out.", "skill"),
    ("{}, enter the profession. This is optional, so send a dot if you don't want to fill it out.", "profession"),
)


@bot.command()
async def create(ctx):
    author = ctx.message.author
    if user_data.has_profile(author.id):
        await ctx.send(
            f"Sorry {author.mention}, you already have a profile registered. Please contact a server administrator to change it.")
        return

    def check(user):
        return user == author

    for question in create_order:
        await ctx.send(question[0].format(author.mention))
        try:
            reply = await bot.wait_for("message", check=check, timeout=600.0)
        except asyncio.TimeoutError:
            await ctx.send(f"{author.mention}, you took more than 10 minutes to reply. Please use the command again.")
            break

        if not reply == ".":
            user_data.set_profile(author.id, question[1], reply)
        else:
            await ctx.send("Skipping")

    await ctx.send(f"{author.mention}, thanks for creating your character! You can now participate in the game.")


# I simplified this
@bot.command(name="inventory", aliases=["inv"])
async def inventory(ctx, usr=None):
    author = ctx.message.author
    if usr:
        usr = ctx.message.author.id


    msg = f"{author.mention}{user_data.get_inv(usr)}"
    await ctx.send(msg)


@bot.command(name="search_inventory", aliases=["search_inv"], hidden=True)
async def search_inventory(ctx, usr=None):
    author = ctx.message.author
    if usr:
        usr = get_id_from_mention(usr)
    else:
        ctx.send(f"{author.mention}, Incorrect usage ``` .search_inventory [user] ```")

    msg = f"{mention_from_id(usr)}{user_data.get_inv(usr)}"
    await ctx.send(msg)


# Rory now we can both do it
@bot.command(name="logout", hidden=True)
async def logout(ctx):
    author = ctx.message.author
    authorid = ctx.message.author.id
    msg = f"{author.mention}, Logging out"
    msg1 = f"{author.mention}, You do not have permission to use this command."
    if admin_data.is_admin(authorid):
        user_data.save()
        await ctx.send(msg)
        await bot.logout()
    else:
        await ctx.send(msg1)


@bot.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if message.author == bot.user:
        return

    user = message.author.id
    user_data.check_usr(user)

    await bot.process_commands(message)

    if 'Fuck' in message.content:
        await message.channel.send('Stop swearing motherfuck')
    else:
        print('no swearing')


@bot.event
async def on_ready():
    print("Successfully logged in")
    print(f"ID: {bot.user.id}\nUsername: {bot.user.name}")
    activity = discord.Activity(name='for .help', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)


if __name__ == "__main__":
    print("Starting...")
    bot.run(TOKEN)
