import io
import unicodedata
import aiohttp
import discord
from discord.ext import commands

class Bigmoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bigmoji(self, ctx, emoji=None):
        """Post a large .png of an emoji"""
        if emoji == None:
            await ctx.send("No emoji to make big...")
        elif emoji[0] == '<':
            # custom Emoji
            name = emoji.split(':')[1]
            emoji_name = emoji.split(':')[2][:-1]
            if emoji.split(':')[0] == '<a':
                # animated custom emoji
                url = 'https://cdn.discordapp.com/emojis/' + emoji_name + '.gif'
                name += '.gif'
            else:
                url = 'https://cdn.discordapp.com/emojis/' + emoji_name + '.png'
                name += '.png'
        else:
            chars = []
            name = []
            for char in emoji:
                chars.append(str(hex(ord(char)))[2:])
                try:
                    name.append(unicodedata.name(char))
                except ValueError:
                    # Sometimes occurs when the unicodedata library cannot
                    # resolve the name, however the image still exists
                    name.append("none")
            name = '_'.join(name) + '.png'
            #url = 'https://twemoji.maxcdn.com/2/72x72/' + '-'.join(chars) + '.png'
            url = 'https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/' + '-'.join(chars) + '.png'

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                #print(url)
                if response.status != 200:
                    await ctx.send('Emoji not found.')
                    return
                
                img = await response.read()
                await session.close()

        img = io.BytesIO(img)
        await ctx.send(file=discord.File(img, name))

async def setup(bot):
    await bot.add_cog(Bigmoji(bot))