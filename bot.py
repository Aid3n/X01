import discord #requirements
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio #requirements
import io
import random
import requests #requirements

client = discord.Client()


@client.event
async def on_ready():
    print('---------------')
    print(' Logged in as')
    print('---------------')
    print(" Join : " + client.user.name)
    print('---------------')
    print('  Created by ')
    print('   Aiden ©  ')
    print('---------------')

@client.event
async def on_message(message):
    await client.change_presence(game=discord.Game(name='X01'))

    channel = message.channel

    if message.content.startswith('.help'):
        emb = (discord.Embed(description="*.invite* -> Link para invitarme a tu server.\n\n*.user* -> Información del usuario mencionado.", colour=000000))
        emb.set_author(name="Subject X-01",icon_url="https://cdn.discordapp.com/attachments/478509969684299786/478509983659720704/AR01..jpg")
        await client.send_message(message.channel, embed=emb)

    if message.content.startswith('.invite'):
        await client.send_message(message.channel,"Link de invitación: " + "https://discordapp.com/oauth2/authorize?client_id=455725168556245003&scope=bot&")

    if message.content.startswith('<@437954268004352010>'):
        await client.send_message(message.channel, "Mi prefijo es _***.***_")

    if message.content.startswith(".icon"):
        await client.send_file(message.channel, 'icon.jpg')

    if message.content.lower().startswith('ola tio'):
        await client.add_reaction(message, '🇴')
        await client.add_reaction(message, '🇱')
        await client.add_reaction(message, '🇦')

    if message.content.lower().startswith('.coin'):
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')

    if message.content.startswith('.user'):
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]
            useravatar = str(user.default_avatar_url).split('.', )[0]

            userembed = discord.Embed(
                title='Nombre de usuario:',
                description=user.name,
                color=FFFF00
            )
            userembed.set_author(
                name="Información del usuario"
            )
            userembed.add_field(
                name='Entró al server el:',
                value=userjoinedat
            )
            userembed.add_field(
                name='Usuario creado el:',
                value=usercreatedat
            )
            userembed.add_field(
                name='Discriminator:',
                value=user.discriminator
            )
            userembed.add_field(
                name='ID del usuario:',
                value=user.id
            )

            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, 'Ese usuario no está en el server')
        except:
            await client.send_message(message.channel, 'Sorry Error :C')
        finally:
            pass

    if message.content.startswith('.version'):
        await client.send_message(channel, '1.0.0')


bot.run(os.environ['BOT_TOKEN'])
