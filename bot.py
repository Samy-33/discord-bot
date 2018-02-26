import discord
import asyncio
import random
import pickle
import os
import requests as rq


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

    elif message.content.startswith('!!addrole'):
        roles = message.content.split()
        if len(roles) == 1:
            await client.send_message(message.channel, 'Please provide a list of roles.')
        else:
            roles_objects = list()

            for role in roles:
                role_object = discord.utils.get(message.server.roles, name=role)
                if role_object:
                    roles_objects.append(role_object)

            await client.add_roles(message.author, *roles_objects)
            await client.send_message(message.channel, 'Roles updated :)')

    elif message.content.startswith('!!yomama'):
        obj = rq.get('http://api.yomomma.info')
        await client.send_message(message.channel, obj.json()['joke'])

    elif message.content.startswith('!!serverinfo'):
        to_send = ''
        for server in client.servers:
            for member in server.members:
                to_send += member.name + '\n'
        await client.send_message(message.channel, to_send)

client.run('Secret-Key-Goes-Here')
