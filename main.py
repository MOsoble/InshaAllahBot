import discord
import os

client = discord.Client()

#@wrapper_function is the equivalent of
#def wrapped_function():
#     pass
# wrapped_function = wrapper_function(wrapped_function)

@client.event
#call backs
async def on_ready():
  print('We have logged in as  {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith('I will') or message.content.startswith('I shall'):
    await message.channel.send('InshaAllah!')

client.run(os.getenv('TOKEN'))