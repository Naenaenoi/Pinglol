from discordwebhook import Discord
import discord
import requests
from discord.ext import commands
from discord.utils import get

discord = Discord(url="https://discord.com/api/webhooks/1061162618921963620/6vGuQsH2JvEfwOel3T6sbvTSDxf4XlvaOVYxrs3GuurLYd7MwM8dhMTxZmjtuaMrwQPc")
discord.post(content="<@318957877681324033>")

"""
bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!")\

@bot.command()
async def ping(ctx):
"""