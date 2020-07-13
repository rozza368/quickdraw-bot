import discord, asyncio
from discord.ext import commands
import data
import bot



user_data = data.UserData()


class Campaign(commands.Cog, name="Campaign"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="start_campaign")
    async def start_campaign(self, ctx):
        if bot.is_owner:
            await ctx.send("Campaign has started")



def setup(bot):
    bot.add_cog(Campaign(bot))
    print("Campaign cog loaded.")