from discord.ext import commands
import discord
import asyncio
import datetime

class ScreamingHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        destination = self.get_destination()
        e = discord.Embed(title="Help", color=discord.Color.blurple(), description="Help for all of ScreamingBot's commands.")
        for i in mapping.values():
            for cmd in i:
                if not cmd.hidden:
                    e.add_field(name=cmd.name, value=str(cmd.help), inline=True)  # change inline to True if you want it to be a grid
        e.set_footer(text="ScreamingBot")
        e.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        await destination.send(embed=e)