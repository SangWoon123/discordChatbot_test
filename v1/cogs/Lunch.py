from discord.ext import commands
import discord
import json
import random

class Lunch(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open('./data/lunch.json','r',encoding='utf-8') as f:
            self.lunchDict=json.load(f)    

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lunch Cog is Ready")

    @commands.command(name="점심추천")
    async def recommand_lunch(self,ctx,arg1=None,arg2=None):
        if arg1 and arg2 == None:
            categories = list(self.lunchDict.keys())
            category = random.choice(categories)
            lunch = random.choice(self.lunchDict[category])
            await ctx.send(f"오늘 점심은 {category}, 그 중에서 {lunch} 어떠세요?")
        else:
            category1 = arg1
            category2= arg2
            lunch1 = random.choice(self.lunchDict[category1])
            lunch2 = random.choice(self.lunchDict[category2])
   
            await ctx.send(f"오늘 점심은 {lunch1} 또는 {lunch2} 어떠세요?")
        
async def setup(client):
    await client.add_cog(Lunch(client))