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
        await client.send_message(channel, '0.2.0')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(messages)
    await client.delete_messages(messages)
    await client.say('Mensajes borrados.')
        
      
client.run(os.environ['BOT_TOKEN'])
