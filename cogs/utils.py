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
        """Shows the latencies for all of ScreamingBot's shards."""
        em = discord.Embed(title="Shard latencies", description="Latencies of all of the working shards.",
                           color=randint(0, 0xFFFFFF))
        for i in self.bot.latencies:
            em.add_field(name=f"Shard {str(i[0])}", value=f"{str(i[1])}ms")
        em.set_footer(text="ScreamingBot")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        await ctx.send(embed=em)

    @commands.command(pass_context=True, hidden=True)
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def changepresence(self, ctx, *, presence: str):
        """Changing the presence of the bot."""
        game = discord.Game(presence)
        await self.bot.change_presence(status=discord.Status.idle, activity=game)
        await ctx.send(":white_check_mark: Changed!")


def setup(bot):
    bot.add_cog(Utils(bot))
