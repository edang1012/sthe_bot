import discord
from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def template(self, ctx, *arg):
        """Get motivated to workout"""
        if arg:
            msg = str(*arg)
            await ctx.send(msg)

            embed = discord.Embed(description = 'ITS TIME MOTHERFUCKER!!!',
                                color = discord.Color.red())
            embed.set_image(url='https://media1.tenor.com/images/316802abc29c277b08bae799b1fbe52c/tenor.gif')
            await ctx.send(embed=embed)

        else:
            await ctx.send("add argument dumbass")


async def setup(bot):
    await bot.add_cog(Template(bot))