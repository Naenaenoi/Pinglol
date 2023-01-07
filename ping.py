import funny
from discordwebhook import Discord
import discord
import requests
from discord.ext import commands
from discord.utils import get

print("input bot url")
print('')
botUrl = str(input())

print('')
print("input user id")
print('')
userId = str(input())

print("Spam this user?")
print('Y/N')
spam = str(input())

discord = Discord(url = botUrl)

if spam == 'Y': 
    while True:
        discord.post(content ="<@{}>" .format(userId))

elif spam == 'N':
    discord.post(content = "<@{}>" .format(userId))

else:
    print(funny)

"""
bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!")\

@bot.command()
async def ping(ctx):
"""