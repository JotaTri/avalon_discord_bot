import discord
from discord.ext import commands
from game import game

"""
Um dia isso vai ser a parte integrada com o discord
TOKEN = ''

client = commands.Bot(command_prefix= '/')

@client.command(pass_context=True)
async def game(ctx):
    print(ctx.channel.id)
    msg_start = 'Starting Avalon Game'
    await ctx.channel.send(msg_start)
    #client.run(TOKEN)
"""

qty = 5
id_discord = ["1", "2", "3", "4", "5"]
name = ["arnaldo", "bernaldo", "cernaldo", "dernaldo", "ernaldo"]
jogo = game(qty, id_discord, name)
jogo.init_quests()