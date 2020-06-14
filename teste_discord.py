import discord
import asyncio
import os
from discord.ext import commands

TOKEN = os.getenv("discord_token")
client = commands.Bot(command_prefix="/")

# game(qty, id_discord, name)

async def my_background_task():
    print("teste1")
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name="teste"))
    print(1)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


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
