from discord.ext import commands
import discord
import random
import csv

class Quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.quizDict={}

        with open('./data/quiz.csv','r',encoding='utf-8') as f:
               reader=csv.reader(f)
               for row in reader:
                    self.quizDict[row[0]]=row[1]

    @commands.command(name="퀴즈")
    async def quiz(self,ctx):
        problemList=list(self.quizDict.keys())
        problem=random.choice(problemList)
        answer=self.quizDict[problem]
        await ctx.send(problem)

        def checkAnswer(message):
            if message.channel==ctx.channel and answer in message.content:
                return True
            else:
                return False
        try:
            await self.client.wait_for("message",timeout=10.0,check=checkAnswer)
            await ctx.send("정답이에요!")
        except asyncio.TimeoutError:
            await ctx.send(f"땡 시간초과입니다! 정답은 {answer}이에요!")


    @commands.Cog.listener()
    async def on_ready(self):
        print("Quiz Cog is Ready")

    # @commands.command(name="퀴즈")
    # async def recommand_lunch(self,ctx):
        
        
async def setup(client):
    await client.add_cog(Quiz(client))