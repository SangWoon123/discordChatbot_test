import discord
from discord.ext import commands
import os
import asyncio




async def main():
    prefix="!"
    intents = discord.Intents.all()
    client=commands.Bot(command_prefix=prefix,intents=intents)
    for filename in os.listdir('./cogs'):
        if '.py' in filename:
            filename=filename.replace('.py','')
            await client.load_extension(f"cogs.{filename}")

    with open('token.txt','r') as f:
        token=f.read()
        
    await client.start(token)
    

    

if __name__=='__main__':
    asyncio.run(main())

