import discord, asyncio
from discord.ext import commands
import data



user_data = data.UserData()


class Characters(commands.Cog, name="Characters"):
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

    # I simplified this
    @bot.command(name="inventory", aliases=["inv"])
    async def inventory(self, ctx):
        admin_command = False
        author = ctx.message.author
        user = str(ctx.message.author.id)

        msg = f"{author.mention}{user_data.get_inv(user, admin_command)}"
        await ctx.send(msg)

    @bot.command(name="search_inventory", aliases=["search_inv"], hidden=True)
    async def search_inventory(self, ctx, usr=None):
        admin_command = True
        author = ctx.message.author
        if usr:
            usr = self.bot.get_id_from_mention(usr)
        else:
            await ctx.send(f"{author.mention}, Incorrect usage ``` .search_inventory [user] ```")

        msg = f"{self.bot.mention_from_id(usr)}{user_data.get_inv(usr, admin_command)}"
        await ctx.send(msg)

    @bot.command(name="register")
    async def register(self, ctx):
        author = ctx.message.author
        msg = f"{author.mention}{user_data.create_id(author.id)}"
        await ctx.send(msg)


def setup(bot):
    bot.add_cog(Characters(bot))
    print("Characters cog loaded.")
