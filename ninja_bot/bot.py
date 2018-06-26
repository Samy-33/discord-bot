import discord
import asyncio
import random
import pickle
import os
import requests as rq
from constants.bot_constants import SECRET_KEY
from services.router import router

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')


@client.event
async def on_message(message):
    if message.content.startswith('!!hey'):
        await client.send_message(message.channel, 'Hey, there.', tts=True)

    elif message.content.startswith('!!yomomma'):
        to_send = router.get_yomomma()({})
        await client.send_message(message.channel, to_send)


client.run(SECRET_KEY)
