import re
import random
import discord
from discord.ext import commands

class msgReply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        #content = message.content.lower().split()
        content = message.content.lower()
        if len(content) < 2:
            return
        
        pattern0 = re.compile(r'(test embed)', re.IGNORECASE)
        pattern1 = re.compile(r'(sigh)+[.]*', re.IGNORECASE)
        pattern2 = re.compile(r'(oh my)', re.IGNORECASE)
        pattern3 = re.compile(r'(keikaku)', re.IGNORECASE)
        pattern4 = re.compile(r'\A(\.\.\.)+[.]*', re.IGNORECASE)
        # \A ensures the following string must start the message
        pattern5 = re.compile(r'(sorry not sorry)', re.IGNORECASE)
        pattern5_1 = re.compile(r'(sorrynotsorry)', re.IGNORECASE)
        pattern5_2 = re.compile(r'(gomenasike)', re.IGNORECASE)
        pattern6 = re.compile(r'(nice)', re.IGNORECASE)
        pattern7 = re.compile(r'(good bot[.!]*)', re.IGNORECASE)
        pattern8 = re.compile(r'(bad bot[.!]*)', re.IGNORECASE)
        pattern9 = re.compile(r'(umu)', re.IGNORECASE)
        pattern10 = re.compile(r'(next (you\'?ll|you\'?re gonna) say|your next (line is|line\'?ll be))', re.IGNORECASE)
        pattern11 = re.compile(r'(meeting)', re.IGNORECASE)
        pattern12 = re.compile(r'(impostor)', re.IGNORECASE)
        
        if re.search(pattern0, content):
            content_split = content.split()
            #msg = "it works!!! shishou"
            #await message.channel.send(msg)
                
            if "embed" in content_split[1]:
                embed = discord.Embed(
                    title = 'Title',
                    description = 'This is a description',
                    color = discord.Color.blue()
                )
                embed.set_footer(text='This is a footer')
                embed.set_image(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
                embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
                embed.add_field(name='Field Name', value='Field Value', inline=False)
                await message.channel.send(embed=embed)

        if re.search(pattern1, content):
            embed = discord.Embed(
                description = 'sigh...\nsai...\nSAIDO CHESTO!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/316802abc29c277b08bae799b1fbe52c/tenor.gif')
            await message.channel.send(embed=embed)
            
        if re.search(pattern2, content):
            embed = discord.Embed(
                description = 'oh my...\nomae...\nOMAE WA MOU SHINDEIRU!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://i.makeagif.com/media/2-21-2015/RDVwim.gif')
            await message.channel.send(embed=embed)
            
        if re.search(pattern3, content):
            msg = "TL's Note: Keikaku means plan."
            await message.channel.send(msg)

        if re.search(pattern4, content):
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_image(url='https://i.imgur.com/RrbvQYz.jpg')
            await message.channel.send(embed=embed)
            
        if re.search(pattern5, content) or re.search(pattern5_1, content) or re.search(pattern5_2, content):
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_image(url='https://i.pinimg.com/236x/81/95/4c/81954cf575ffa7bd8b573efc848c92c0.jpg')
            await message.channel.send(embed=embed)
            
        if re.search(pattern6, content):
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/392da4650dfa83b3055069e39ad74b45/tenor.gif?itemid=7319727')
            await message.channel.send(embed=embed)
            
        if re.search(pattern7, content):
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_image(url='https://i.imgur.com/pikZ3a1.gif')
            await message.channel.send(embed=embed)
            
        if re.search(pattern8, content):
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_image(url='https://i.imgur.com/HrbaFyJ.gif')
            await message.channel.send(embed=embed)
            
        if re.search(pattern9, content):
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_image(url='https://i.imgur.com/PRa4ukr.jpg')
            await message.channel.send(embed=embed)
            
        if re.search(pattern10, content):
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_image(url='https://i.imgflip.com/3hwwle.png')
            await message.channel.send(embed=embed)
            
        if re.search(pattern11, content):
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/a496903c9724d2b4fdbf228d74f6dd25/tenor.gif')
            await message.channel.send(embed=embed)
        
        if re.search(pattern12, content):
            rand = random.randint(0, 2)
            
            embed = discord.Embed(
                color = discord.Color.red()
            )
            if rand == 0:
                embed.set_image(url='https://media1.tenor.com/images/a0d13ec25f9774f155b6cd5ebf12a6c8/tenor.gif')
            if rand == 1:
                embed.set_image(url='https://media1.tenor.com/images/ef4993b593954811a0c0a1c98af698a3/tenor.gif')
            if rand == 2:
                embed.set_image(url='https://attachments.f95zone.to/2020/08/798465_AS_Impostor.gif')
            await message.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(msgReply(bot))