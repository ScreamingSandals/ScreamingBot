from discord.ext import commands
import discord
import asyncio
import datetime


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def brokenshop(self, ctx):
        """Useful links for fixing a broken shop file."""
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
        """A link for the Jenkins page."""
        em = discord.Embed(title="ScreamingSandals Jenkins", url="https://ci.screamingsandals.org")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)

    @commands.command(pass_context=True)
    async def addsign(self, ctx):
        """Info about adding a join/leave sign."""
        em = discord.Embed(title="Adding a join/leave sign")
        em.add_field(name="Sign contents", value="`[BedWars]`\n`arenaname`")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)

    @commands.command(pass_context=True)
    async def resources(self, ctx):
        """Info about editing resources in the config file."""
        em = discord.Embed(title="Editing resources")
        em.add_field(name="Adding diamond and emerald generators", value="See the picture.", inline=False)
        em.add_field(name="Changing the spawning rate of the generators",
                     value="Change the interval value for each resource.", inline=False)
        em.set_image(url="https://cdn.discordapp.com/attachments/703770486621995100/793596588505038848/resources.png")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)

    @commands.command(pass_context=True)
    async def language(self, ctx):
        """Info about translating BedWars and the language file location."""
        em = discord.Embed(title="Language")
        em.add_field(name="Translating",
                     value="You can translate the plugin to your language with [Weblate](https://weblate.screamingsandals.org).")
        em.add_field(name="Language file",
                     value="The language file for 0.2.15 is [here](https://github.com/ScreamingSandals/BedWars/tree/bd12385f7c2e349b76feb2760a0db6712b7b1763/plugin/src/main/resources/languages).\nDownload the language files for BW and put them in the /plugins/bedwars/languages folder to use them.")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)

    @commands.command(pass_context=True)
    async def java11(self, ctx):
        """Info about upgrading to Java 11."""
        em = discord.Embed(title="Java 11", description="Here's instructions on how to upgrade to Java 11.")
        em.add_field(name="Docs", value="See our [docs](https://docs.screamingsandals.org) for instructions.")
        em.add_field(name="AdoptOpenJDK download", value="Download AdoptOpenJDK [here](https://adoptopenjdk.net/).")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)

    @commands.command(pass_context=True, aliases=["1.8", "1.8.x", "fuckoldversions", "fuck1.8"])
    async def versions(self, ctx):
        """Info on versions that SBW and SBA support."""
        em = discord.Embed(title="Versions")
        em.add_field(name="Versions", value="SBW and SBA support versions ranging from 1.9.4 to the latest.",
                     inline=False)
        em.add_field(name="1.8.x",
                     value="We won't support 1.8.x **ever**, because it makes our work harder.\nWe strongly recommend to use the latest version of Minecraft along with [OldCombatMechanics](https://www.spigotmc.org/resources/oldcombatmechanics-disable-1-9-hit-cooldown.19510/) if you want the 1.8.x combat.",
                     inline=False)
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)

    @commands.command(pass_context=True)
    async def repo(self, ctx):
        """A link for the ScreamingSandals repository."""
        em = discord.Embed(title="ScreamingSandals repo", url="https://repo.screamingsandals.org")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)

    @commands.command(pass_context=True, aliases=["papi", "placeholderapi"])
    async def placeholders(self, ctx):
        """A link for SBW PlaceholderAPI placeholders."""
        em = discord.Embed(title="Placeholders for ScreamingBedWars",
                           url="https://github.com/ScreamingSandals/BedWars/wiki/PlaceholderAPI-placeholders")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)

    @commands.command(pass_context=True, aliases=["javadoc", "jd"])
    async def javadocs(self, ctx):
        """A link for the SBW Javadocs."""
        em = discord.Embed(title="ScreamingBedWars Javadocs", url="https://jd.screamingsandals.org")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)

    @commands.command(pass_context=True, aliases=["bwprefix"])
    async def sbwprefix(self, ctx):
        """Info about changing the chat prefix of SBW."""
        em = discord.Embed(title="Prefix",
                           description="You can change prefix per game via\n`/bw admin <arena> customprefix &6My Awesome Prefix`\n\nOr you can change it by modifying the language files.")
        em.timestamp = datetime.datetime.now(tz=datetime.timezone.utc)
        em.set_footer(text="ScreamingBot")
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Help(bot))
