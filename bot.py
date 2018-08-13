import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Ready.')

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('.version'):
        await client.send_message(channel, '0.1.0')

client.run(os.environ['BOT_TOKEN'])
