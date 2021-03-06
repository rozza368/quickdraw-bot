import discord, asyncio
from discord.ext import commands
import data
import bot



user_data = data.UserData()


class Register(commands.Cog, name="Register"):
    def __init__(self, bot):
        self.bot = bot

        # This needs to be fixed
        self.create_order = (
            ("{}, enter the name.", "name"),
            ("{}, enter the age. It must be higher than 20.", "age"),
            ("{}, enter the gender.", "gender"),
            ("{}, enter the county.", "county"),
            ("{}, enter the physical description.", "physical"),
            ("{}, enter the personality description.", "personality"),
            ("{}, enter the special skill. This is optional, so send a dot if you don't want to fill it out.", "skill"),
            ("{}, enter the profession. This is optional, so send a dot if you don't want to fill it out.",
             "profession"),
        )

    @commands.command()
    async def create(self, ctx):
        author = ctx.message.author
        if user_data.has_profile(author.id):
            await ctx.send(
                f"Sorry {author.mention}, you already have a profile registered. Please contact a server administrator to change it.")
            return

        def check(user):
            return user == author

        for question in self.create_order:
            await ctx.send(question[0].format(author.mention))
            try:
                reply = await self.bot.wait_for("message", check=check, timeout=600.0)
            except asyncio.TimeoutError:
                await ctx.send(
                    f"{author.mention}, you took more than 10 minutes to reply. Please use the command again.")
                break

            if not reply == ".":
                user_data.set_profile(author.id, question[1], reply)
            else:
                await ctx.send("Skipping")

        await ctx.send(f"{author.mention}, thanks for creating your character! You can now participate in the game.")



def setup(bot):
    bot.add_cog(Register(bot))
    print("Characters cog loaded.")
