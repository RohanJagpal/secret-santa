from discord.ext.commands import Cog, command
from random import choice

class Santa(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def santa(self, ctx):
        pass