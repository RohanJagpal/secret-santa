from discord import Embed
from discord.ext import commands
from random import choice
import json
import asyncio


class SantaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def santa(self, ctx):
        with open("users.json", "r") as jsonfile:
            currentList = json.load(jsonfile)["users"]
        done = []
        for user in currentList:
            chosen = user
            while chosen == user or chosen in done:
                chosen = choice(currentList)
            done.append(chosen)
            chosen = await self.bot.fetch_user(chosen)
            user = await self.bot.fetch_user(user)
            embed = Embed(
                title="Secret Santa",
                description=f"You have been given {chosen.mention} for secret santa!",
                color=1997100,
            )
            try:
                await user.send(embed=embed)
            except:
                embed = Embed(
                    title="An error occurred!",
                    description=f"I could not send a message to {user.mention}. Please check that you have DMs turned on.",
                    color=12783382,
                )
                await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def join(self, ctx):
        with open("users.json", "r+") as jsonfile:
            currentList = json.load(jsonfile)
        if ctx.author.id in currentList["users"]:
            return
        currentList["users"].append(ctx.author.id)
        with open("users.json", "w") as jsonfile:
            jsonfile.write(json.dumps(currentList))
        await ctx.message.delete()
        embed = Embed(
            title="Success!",
            description=f"{ctx.author.mention} You joined the secret santa list!",
            color=1997100,
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(3)
        await msg.delete()

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        with open("users.json", "r") as jsonfile:
            currentList = json.load(jsonfile)
        if not ctx.author.id in currentList["users"]:
            return
        currentList["users"].remove(ctx.author.id)
        with open("users.json", "w") as jsonfile:
            jsonfile.write(json.dumps(currentList))
        await ctx.message.delete()
        embed = Embed(
            title="Success!",
            description=f"{ctx.author.mention} You left the secret santa list!",
            color=12783382,
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(3)
        await msg.delete()

    @commands.command()
    async def listusers(self, ctx):
        with open("users.json", "r") as jsonfile:
            currentList = json.load(jsonfile)["users"]
        desc = ""
        for user in currentList:
            desc += f"{await self.bot.fetch_user(user).mention}\n"
        embed = Embed(
            title="Current Users",
            description=desc,
            color=1997100
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(6)
        await msg.delete()


def setup(bot):
    bot.add_cog(SantaCog(bot))
