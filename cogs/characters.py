import discord, asyncio
from discord.ext import commands
import data
import bot

user_data = data.UserData()


class Characters(commands.Cog, name="Characters"):
    def __init__(self, bot):
        self.bot = bot

    # I simplified this
    @commands.command(name="inventory", aliases=["inv"])
    async def inventory(self, ctx):
        admin_command = False
        author = ctx.message.author
        user = str(ctx.message.author.id)

        msg = f"{author.mention}{user_data.get_inv(user, admin_command)}"
        await ctx.send(msg)

    @commands.command(name="search_inventory", aliases=["search_inv"], hidden=True)
    async def search_inventory(self, ctx, usr=None):
        admin_command = True
        author = ctx.message.author
        if usr:
            usr = self.bot.get_id_from_mention(usr)
        else:
            await ctx.send(f"{author.mention}, Incorrect usage ``` .search_inventory [user] ```")

        msg = f"{self.bot.mention_from_id(usr)}{user_data.get_inv(usr, admin_command)}"
        await ctx.send(msg)

        # I simplified this

    @commands.command(name="mimic", hidden=True)
    async def mimic(self, ctx):
        if bot.is_owner:
            while True:
                stuff = input('Mimic:')
                await ctx.send(stuff)

    @commands.command(name="logout", hidden=True)
    async def logout(self, ctx):
        msg = f"{ctx.message.author.mention}, Logging out"
        msg1 = f"{ctx.message.author.mention}, You do not have permission to logout me!"
        if bot.is_owner(ctx.message.author.id):
            user_data.save()
            await ctx.send(msg)

        else:
            await ctx.send(msg1)


def setup(bot):
    bot.add_cog(Characters(bot))
    print("Register cog loaded.")
