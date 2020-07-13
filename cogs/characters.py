import discord, asyncio
from discord.ext import commands
import data



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



def setup(bot):
    bot.add_cog(Characters(bot))
    print("Register cog loaded.")
