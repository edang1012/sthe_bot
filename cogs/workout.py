import discord
from discord.ext import commands

class Workout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def workout(self, ctx, arg=None):
        """Get motivated to workout"""
        if arg == None:
            await ctx.send("add argument dumbass")
        else:    
            msg = str(arg)
            await ctx.send(msg)

            embed = discord.Embed(description = 'ITS TIME MOTHERFUCKER!!!',
                                color = discord.Color.red())
            embed.set_image(url='https://media1.tenor.com/images/316802abc29c277b08bae799b1fbe52c/tenor.gif')
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Workout(bot))