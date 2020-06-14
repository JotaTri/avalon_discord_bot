import discord
import asyncio
import os
from discord.ext import commands

TOKEN = os.getenv("discord_token")
client = commands.Bot(command_prefix="/")


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


client.loop.create_task(my_background_task())
client.run(TOKEN)
