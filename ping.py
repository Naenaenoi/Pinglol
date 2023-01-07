from discordwebhook import Discord
import discord
import requests
from discord.ext import commands
from discord.utils import get

discord = Discord(url="https://discord.com/api/webhooks/1061192583155560589/bjb50hoqxShd1IV6DdHRnld_UfgyAaExc69ysOUU9pFXeOvufBBrTajiCZhpQ_jFlY-i")
discord.post(content="<@318957877681324033>")

"""
bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!")\

@bot.command()
async def ping(ctx):
"""