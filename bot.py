import discord
from bot.TOKEN import TOKEN

class main:
    def __init__(self):
        # Main
        print('init')
        self.client = discord.Client()  # starts the discord client

MainMF = main()
MainMF.client.run(TOKEN)