import discord
from discord.ext import commands
from game import game

TOKEN = 'NjkwOTgxOTgzNTA5MjgyOTM2.XnZXlA.8fKAxVq51-JQJSQ2RYYcC6I9dLE'

client = commands.Bot(command_prefix= '/')

@client.command(pass_context=True)
async def game(ctx):
    print(ctx.channel.id)
    msg_start = 'Starting Avalon Game'
    await ctx.channel.send(msg_start)



client.run(TOKEN)