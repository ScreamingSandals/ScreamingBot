from discord.ext import commands
import discord
import asyncio
import datetime

class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def brokenshop(self, ctx):
		em = discord.Embed(
			title="Broken shop", description="**I can't use my shop!**\n"
			"Check your *YAML* format! Use the following links.\n"
			"[Link 1 - SimpleInventories Wiki Page](https://github.com/ScreamingSandals/SimpleInventories/wiki/)\n"
			"[Link 2 - Materials](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html)\n"
			"[Link 3 - YAML Validator](https://yamlchecker.com/)"
		)
		em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
		em.set_footer(text="ScreamingBot")
		await ctx.send(embed=em)

	@commands.command(pass_context=True)
	async def jenkins(self, ctx):
		em = discord.Embed(title="ScreamingSandals Jenkins", url="https://ci.screamingsandals.org")
		em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
		em.set_footer(text="ScreamingBot")
		await ctx.send(embed=em)


def setup(bot):
	bot.add_cog(Help(bot))
