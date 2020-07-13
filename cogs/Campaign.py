import discord, asyncio
from discord.ext import commands
import data
import bot
import os



user_data = data.UserData()


class Campaign(commands.Cog, name="Campaign"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="start_campaign")
    async def start_campaign(self, ctx):
        if bot.is_owner:
            if not os.path.isfile('campaign.txt'):
                with open('campaign.txt', 'w') as campaign:
                    campaign.write(1)
                    campaign.close()
                    with open('campaign.txt', 'r') as campaign:
                        hellp = campaign.read()
                        await ctx.send(f"Campaign {hellp} has started")
            else:
                with open('campaign.txt', 'r') as campaign:
                    hellp = campaign.read()
                    campaign.close()
                    with open('campaign.txt', 'w') as campaign:
                        hellp = str(int(hellp) + 1)
                        campaign.write(hellp)
                        campaign.close()
                        with open('campaign.txt', 'r') as campaign:
                            hellp = campaign.read()
                            campaign.close()

                        await ctx.send(f"Campaign {hellp} has started")





def setup(bot):
    bot.add_cog(Campaign(bot))
    print("Campaign cog loaded.")