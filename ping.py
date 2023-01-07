import discord
import requests
from discord.ext import commands
from discord.utils import get

client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!")

"""
@client.command()
async def ping(ctx):
    user = get(ctx.guild.members, name = 'yukari-sensei!!!!!!!!')
    await ctx.send(f"{user.mention}")


@client.command()
async def variable_name(ctx, user: discord.User):
    await ctx.send({user.mention})
    
    import requests
 """

def ping(channelId, userId, message, token):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channelId)
    header = {"authorization": token}
    data = {"content": "<@{}> {}".format(userId, message)}
 
    r = requests.post(url, headers=header, data=data)
    print(r.status_code)

ping('733430536080457741', '486708317570203649', 'yo', 'NDg2NzA4MzE3NTcwMjAzNjQ5.GQhQDY.6FnvnG_Oy3uLI6W9xvhbuWVbY-_g4ikbhbm-Sc')