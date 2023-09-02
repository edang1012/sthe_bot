import re
from discord.ext import commands


class Wat(commands.Cog):

    """Repeat messages when other users are having trouble hearing"""

    def __init__(self, bot):
        self.bot = bot

    # Come up with a new method to ignore bot commands
    @commands.Cog.listener()
    async def on_message(self, message):
        # ignore messages from bot
        if message.author == self.bot.user:
            return
        
        # ignore message with >1 words
        content = message.content.lower().split()
        if len(content) != 1:
            return
        
        # regex for variation of what
        pattern = re.match(r"wh?[aou]t$", content[0])
        if pattern:
            async for check in message.channel.history(limit=5, before=message):
                author  = check.author
                name    = author.display_name
                content = check.clean_content

                if author != message.author and author != self.bot.user:
                    emoji   = "\N{CHEERING MEGAPHONE}"
                    msg     = "{0} said, **{1}   {2}**".format(name, emoji,content)
                    await message.channel.send(msg)
                    break

async def setup(bot):
    await bot.add_cog(Wat(bot))