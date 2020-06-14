import discord
import os
import asyncio
from discord.ext import commands
TOKEN = "NTk1Mzc4Mzk4MDcxNzUwNzU3.XuWFAg.s5NXpmLo-pYZWmAX5_5PeG_Xv4o"
client = commands.Bot(command_prefix= '!')

TOKEN = os.getenv("discord_token")
client = commands.Bot(command_prefix="/")

# game(qty, id_discord, name)

async def my_background_task():
    print("teste1")
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name="teste"))
    print(1)


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


@client.command(name='vote', pass_context=True)
async def new_vote(ctx, arg):
    yes_list = ['sim', 'yep', 'claro', 'sure', '1', 'um']
    no_list = ['não', 'nao', 'no', 'nope']
    # game_round = game.round()
    print(ctx.author)
    print(ctx.author.display_name)
    if arg.lower() in yes_list:
        await ctx.send('vote sim')
    elif arg.lower() in no_list:
        await ctx.send('vote não')
    else:
        await ctx.send('seu bosta')
    # print(message)


client.loop.create_task(my_background_task())
client.run(TOKEN)
client.run(TOKEN)
