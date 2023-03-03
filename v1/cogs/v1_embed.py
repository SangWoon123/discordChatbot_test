from discord.ext import commands
import discord

class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("하루예측 Cog is Ready")
        
    @commands.command(name = "하루예측")
    async def embed(self, ctx):
        # 소개말
        embed=discord.Embed(
        title="안녕하세요. Sentisys 입니다.",
        description="Sentisys는 비트코인 커뮤니티를 분석한 서비스 제공자입니다.",
        color=discord.Color.yellow()
        )

        # 링크
        embed.set_author(
        name="디시인사이드 비트코인 갤러리 결과 바로보기", 
        url="https://cafe.naver.com/codeuniv", 
        icon_url="https://source.unsplash.com/random")

        # 이미지
        embed.set_image(
            url="https://velog.velcdn.com/images/dlsdud9098/post/df02a0b9-a145-4a90-abab-ea85b67311f9/image.png"
        )

        await ctx.send(embed=embed)


        

async def setup(client):
    await client.add_cog(Embed(client))