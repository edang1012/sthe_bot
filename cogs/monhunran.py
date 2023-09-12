#import stuff

#ReadMonstersSheetCell and ReadWeaponsSheetCell are made up commands that are meant to be replaced with however you actually grab data from a cell
#there's a lot of adding strings together to correlate to cells in the spreadsheet.  Not sure if it works that way
#could definitely make the switch skill choosing cleaner

#variables that are strings to be sent:
#MonHunt = [Type of Hunt] [Monster] eg Hazard Primal Malzeno
#Weapon = Player 1's Weapon
#P2_SS3_ = Player 2's Switch Skill 3
#_letter refers to A1 format column

import os
import random
from openpyxl import load_workbook
import discord
from discord.ext import commands
class MonHunRan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def monhunran(self, ctx, arg):

        workbook = load_workbook(filename="monhunrandata.xlsx")

        MonSheet = workbook["Monsters"]
        WPSheet = workbook["Weapons"]
        KinSheet = workbook["Kinsects"]
        LBGSheet = workbook["LBG Mod"]
        HBGSheet = workbook["HBG Mod"]

        MonRNG = random.randint(2, 72) #71 monsters.  First row is the 'Monster' header.  Rows 2-72 are monster names
        MonRow = 'A' + str(MonRNG) #Adds MonRNG number as a string to A.  A21 to correlate to Cell A21 in the Google Sheet
        Mon = MonSheet[MonRow].value #however you read a cell as a string

        HuntRNG = HuntRNG = int(1 + MonSheet['B' + str(MonRNG)].value + MonSheet['C' + str(MonRNG)].value) #RNG range = 1 = column B = column C
        Hunt_Type = (random.randint(1,HuntRNG)) #RNG from 1 to HuntRNG
        if Hunt_Type == 1:
            MonHunt = 'Standard MR ' + Mon
        elif Hunt_Type == 2:
            MonHunt = 'Afflicted ' + Mon
        else:
            MonHunt = 'Hazard ' + Mon

        def weaponize(players):
            WeaponRNG = random.randint(2,15) #see MonRNG but Weapons
            WeaponRow = str(WeaponRNG)
            Weapon = WPSheet['A' + WeaponRow].value
            SS1_RNG = random.randint(1,2)
            if SS1_RNG == 1:
                SS1_letter = 'B'
            else: 
                SS1_letter = 'C'
            SS1 = WPSheet[str(SS1_letter + WeaponRow)].value
            SS2_RNG = random.randint(1,2)
            if SS2_RNG == 1:
                SS2_letter = 'D'
            else:
                SS2_letter = 'E'
            SS2 = WPSheet[str(SS2_letter + WeaponRow)].value
            SS3_RNG = random.randint(1,2)
            if SS3_RNG == 1:
                SS3_letter = 'F'
            else:
                SS3_letter = 'G'
            SS3 = WPSheet[str(SS3_letter + WeaponRow)].value
            SS4_RNG = random.randint(1,3)
            if SS4_RNG == 1:
                SS4_letter = 'H'
            elif SS4_RNG == 2:
                SS4_letter = 'I'
            else:
                SS4_letter = 'J'
            SS4 = WPSheet[str(SS4_letter + WeaponRow)].value
            SS5_RNG = random.randint(1,2)
            if SS5_RNG == 1:
                SS5_letter = 'K'
            else:
                SS5_letter = 'L'
            SS5 = WPSheet[str(SS5_letter + WeaponRow)].value
            print(Weapon)
            print(SS1)
            print(SS2)
            print(SS3)
            print(SS4)
            print(SS5)
            remaining = players - 1
            if remaining > 0:
                weaponize(remaining)
            else: return
                



#embed = discord.Embed(
#   description = print(MonHunt)),
#   color = discord.Color.red()
#return embed

#format and send MonHunt, Weapon, SS1_-5, P2_Weapon, P2_SS1_-5 As a message

#MonHunt = [Type of Hunt] [Monster] eg Hazard Primal Malzeno
#Weapon = Player 1's Weapon
#P2_SS3 = Player 2's Switch Skill 3

async def setup(bot):
    await bot.add_cog(MonHunRan(bot))