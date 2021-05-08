import discord
from discord.ext import commands
import asyncio
import datetime
from random import randint


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def latency(self, ctx):
        em = discord.Embed(title="Shard latencies", description="Latencies of all of the working shards.",
                           color=randint(0, 0xFFFFFF))
        for i in self.bot.latencies:
            em.add_field(name=f"Shard {str(i[0])}", value=f"{str(i[1])}ms")
        em.set_footer(text="ScreamingBot")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Utils(bot))
