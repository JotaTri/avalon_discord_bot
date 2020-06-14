import discord
import os
import asyncio
from discord.ext import commands
TOKEN = "NTk1Mzc4Mzk4MDcxNzUwNzU3.XuWFAg.s5NXpmLo-pYZWmAX5_5PeG_Xv4o"
client = commands.Bot(command_prefix= '!')

# Bot tester
@client.event
async def on_ready():
    print("Bot alive!")

@client.command(name = "start")
async def on_message(message):
    # we do not want the bot to reply to itself
    await message.send('O jogo começou!')

@client.command(name = "join", pass_context=True)
async def joinMemberId(ctx): 
    userId = ctx.author.id
    userName = ctx.author.display_name
    # await ctx.send("ID: {} \n Nome: {}".format(str(userId), str(userName)))
    vagabonds = {userId:userName}
    return vagabonds


client.run(TOKEN)