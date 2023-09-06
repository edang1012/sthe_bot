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
    async def addseq(self, ctx, word=None, emoji=None):
        """Add a sequence of reactions to a keyword/phrase
        Usage:  .addseq <keyword> <emote(s)>
                pass a keyword or keyphrase(in quotations) to <keyword>
                pass an emoji or emojis (in quotations, separated by spaces) to <emoji>
                also update this to make phrases you bum..."""
        if (word == None) or (emoji == None):
            await ctx.send("Wrong format idiot")
        else:
            message = ctx.message
            await self.create_reaction_sequence(message, word, emoji)

    @commands.has_permissions(manage_guild=True)
    @commands.command()
    async def remseq(self, ctx, word):
        """Remove a sequence of reactions to a keyword/phrase
        Usage:  .remseq <keyword>
                pass a keyword or keyphrase(in quotations) to <keyword>"""
        if (word == None):
            await ctx.send("Wrong format idiot")
        else:
            message = ctx.message
            await self.remove_reaction_sequence(message, word)

    @commands.command()
    async def listseq(self, ctx):
        """List reactions for this server"""
        #print(self.react_dict)
        list_msg = "Smart Reactions for Smash the Heavens:\n" + "[keyword: emotes] \n"
        for react in self.react_dict:
            list_msg = list_msg + "\n" + react + ": " + self.react_dict[react]
        await ctx.send(list_msg)

    async def create_reaction_sequence(self, message, word, emoji):
        #load latest changes from file
        if os.path.isfile(data_path):
            #print("loading file")
            with open(data_path) as infile:
                self.react_dict = json.load(infile)

        if word in self.react_dict:
            await message.channel.send("This reaction sequence already exists.")
            return
        else:
            self.react_dict.update({word: emoji})
        
        await message.channel.send("Successfully added this reaction sequence.")

        with open(str(data_path), "w") as outfile:
            json.dump(self.react_dict, outfile)
          
    async def remove_reaction_sequence(self, message, word):
        #load latest changes from file
        if os.path.isfile(data_path):
            #print("loading file")
            with open(data_path) as infile:
                self.react_dict = json.load(infile)

        if word not in self.react_dict:
            await message.channel.send("This reaction sequence doesn't exists.")
            return
        else:
            del self.react_dict[word]
        
        await message.channel.send("Successfully deleted this reaction sequence.")

        with open(str(data_path), "w") as outfile:
            json.dump(self.react_dict, outfile)
      
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.react_dict == {}:
            return
        if message.author == self.bot.user:
            return

        msg_arr = message.content.lower().split()
        for word in msg_arr:
            if word in self.react_dict:
                
                try:
                    #split emoji list into a list
                    reacts = self.react_dict[word].split()

                    for i in reacts:
                        await message.add_reaction(i)
                        
                except discord.errors.Forbidden:
                    pass
                except discord.errors.InvalidArgument:
                    pass

async def setup(bot):
    await bot.add_cog(SeqReact(bot))