from os import environ
from discord import Intents, Activity, ActivityType, Status, __version__
from discord.ext import commands
from santa import Santa
from dotenv import load_dotenv

load_dotenv()

intents = Intents.default()

bot = commands.Bot(command_prefix="!santa", intents=intents)

bot.add_cog(Santa(bot))


@bot.event
async def on_ready():
    print(
        f"\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {__version__}\n"
    )

    activity = Activity(name="with your mum", type=ActivityType.playing)
    await bot.change_presence(status=Status.idle, activity=activity)
    print("Successfully logged in and booted...!")


bot.run(environ.get("TOKEN"))
