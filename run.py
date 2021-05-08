from discord.ext import commands
import discord
import asyncio
from os import environ
from dotenv import load_dotenv
from libs.helpcommand import ScreamingHelpCommand
import datetime

load_dotenv()
token = environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
# intents.members = True

bot = commands.AutoShardedBot(command_prefix="?", intents=intents)
bot.help_command = ScreamingHelpCommand()

@bot.event
async def on_ready():
	bot.load_extension("cogs.utils")
	bot.load_extension("cogs.help")
	print("Bot loaded!")

@bot.event
async def on_command_error(ctx, error):
    e = discord.Embed(title="Exception", color=0xe74c3c,
                      description="An exception was raised and the processing was halted.")
    e.add_field(name="Content", value=f"`{str(error)}`")
    e.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
    e.set_footer(text="ScreamingBot")
    await ctx.send(embed=e)

bot.run(token)
