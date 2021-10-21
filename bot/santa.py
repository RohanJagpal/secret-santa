from discord import Embed
from discord.ext.commands import Cog, command
from random import choice
import json


class Santa(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def santa(self, ctx):
        with open('users.json', 'w+') as f:
            currentList = json.load(f)
            for user in currentList:
                chosen = user
                while chosen == user:
                    chosen = choice(currentList)

                chosen = self.bot.getUser(chosen)
                embed = Embed(
                    title="Secret Santa",
                    description=f"You have been given <@{chosen.id}> for secret santa!",
                    color=1997100
                )
                try:
                    await user.send(embed=embed)
                except:
                    embed = Embed(
                        title="An error occurred!",
                        description=f"I could not send a message to <@{user.id}>. Please check that you have DMs turned on.",
                        color=12783382
                    )
                    await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @command()
    async def join(self, ctx):
        with open('users.json', 'w+') as f:
            currentList = json.load(f)
            currentList.append(ctx.author.id)
            f.write(json.dump(currentList))
        await ctx.message.delete()
        
    @command()
    async def leave(self, ctx):
        with open ('users.json', 'w+') as f:
            currentList = json.load(f)
            currentList.remove(ctx.author.id)
            f.write(json.dump(currentList))
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Santa(bot))
