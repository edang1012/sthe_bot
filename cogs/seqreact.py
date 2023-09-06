import json
import os
import copy
import discord
from discord.ext import commands

data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'seqreact', 'seqreact.json')

class SeqReact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.react_dict = {}
        if os.path.isfile(data_path):
            print("loading file")
            with open(data_path) as infile:
                self.react_dict = json.load(infile)

    @commands.has_permissions(manage_guild=True)
    @commands.command()
    async def addseq(self, ctx, word, emoji):
        """Add a sequence of reactions to a keyword/phrase
        Usage:  
                pass a keyword or keyphrase(in quotations) to <word>
                pass an emoji or emojis (in quotations, separated by spaces) to <emoji>
                also update this to make phrases you bum..."""
        
        guild = ctx.message.guild
        message = ctx.message
        await self.create_reaction_sequence(guild, message, word, emoji)

    @commands.command()
    async def listseq(self, ctx):
        """List reactions for this server"""
        print(self.react_dict)
        await ctx.send(self.react_dict)
        """emojis = await self.conf.guild(ctx.guild).reactions()
        msg = f"Smart Reactions for {ctx.guild.name}:\n"
        for emoji in emojis:
            for command in emojis[emoji]:
                msg += f"{emoji}: {command}\n"
        for page in pagify(msg, delims=["\n"]):
            await ctx.send(msg)"""

    async def create_reaction_sequence(self, guild, message, word, emoji):
        #load latest changes from file
        if os.path.isfile(data_path):
            print("loading file")
            with open(data_path) as infile:
                self.react_dict = json.load(infile)

        print(word)
        if word in self.react_dict:
            await message.channel.send("This reaction sequence already exists.")
            return
        else:
            self.react_dict.update({word: emoji})
        
        await message.channel.send("Successfully added this reaction sequence.")

        with open(str(data_path), "w") as outfile:
            json.dump(self.react_dict, outfile)


    """        
    async def remove_reaction_sequence(self, guild, word, emoji, message):
        try:
            reactions = await self.conf.guild(guild).reactions()
            
            if emoji in reactions:
                if word.lower() in reactions[emoji]:
                    reactions[emoji].remove(word.lower())
                    await self.conf.guild(guild).reactions.set(reactions)
                    await message.channel.send("Removed this reaction sequence.")
                else:
                    await message.channel.send("That sequence is not for that word/phrase")
            else:
                await message.channel.send("There is no sequence to delete.")

        except (discord.errors.HTTPException, discord.errors.InvalidArgument):
            await message.channel.send("Uh oh, something bad happened...")
            
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild:
            return
        if message.author == self.bot.user:
            return
        guild = message.guild
        reacts = copy.deepcopy(await self.conf.guild(guild).reactions())
        if reacts is None:
            return
        words = message.content.lower().split()
        for emoji in reacts:
            if set(w.lower() for w in reacts[emoji]).intersection(words):
                try:
                    #split emoji list into a list
                    emotes = emoji.split()

                    for i in emotes:
                        await message.add_reaction(i)
                        
                except discord.errors.Forbidden:
                    pass
                except discord.errors.InvalidArgument:
                    pass"""

    @commands.command()
    async def seq_temp(self, ctx, *arg):
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
    await bot.add_cog(SeqReact(bot))