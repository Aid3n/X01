import discord
from discord.ext import commands

TOKEN = 'NDU1NzI1MTY4NTU2MjQ1MDAz.DlIKAw.TSNkW0vnVMtfJUnXne6ZWiC39cA'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Ready.')

client.run(TOKEN)
