import discord
import os
from game import Game
from discord.ext import commands

TOKEN = os.getenv("discord_token")
client = commands.Bot(command_prefix="/")

game = Game()


async def my_background_task():
    print("teste1")
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name="teste"))
    print(1)


# Bot tester
@client.event
async def on_ready():
    print("Bot alive!")


@client.command(name="start")
async def on_message(message):
    await message.send('O jogo começou!')


@client.command(name="begin")
async def start_game(message):
    game.shuffle_players()
    await message.send('O jogo começou de vdd agora galerinha!')
    print(game.char)


@client.command(name="join", pass_context=True)
async def join_member_id(ctx):
    userId = ctx.author.id
    userName = ctx.author.display_name

    vagabonds = {
        'discord_id': userId,
        'discord_name': userName
        }

    game.join_game(vagabonds)
    print(game.players_info)


@client.command(name='vote', pass_context=True)
async def new_vote(ctx, arg):
    yes_list = ['sim', 'yep', 'claro', 'sure', '1', 'um']
    no_list = ['não', 'nao', 'no', 'nope', '0', 'zero']

    character = game.get_character(ctx.author)

    if arg.lower() in yes_list:
        await ctx.send('vote sim')
        character.quest_vote = True
    elif arg.lower() in no_list:
        await ctx.send('vote não')
        character.quest_vote = False
    else:
        await ctx.send('@{}, seu voto não existe!!!')


client.loop.create_task(my_background_task())
client.run(TOKEN)
client.run(TOKEN)
