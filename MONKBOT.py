import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print(f'{client.user} MONKE MONKE MONKE MONKE')

@client.command(aliases=["monke", "MONKE"])
async def MONKESpam(ctx):
    await ctx.send("MONKE")

@client.command()
async def give(ctx):
    await ctx.send("I give u :banana:.")

@client.command(aliases=["github", "qweriop"])
async def qweri0p(ctx):
    await ctx.send("https://github.com/qweri0p/MONKE-BOT")

@client.command()
async def takeover(ctx):
    await ctx.send("THE WORLD HAS BEEN DOMINATED BY MONKE!!!")

client.run(TOKEN)