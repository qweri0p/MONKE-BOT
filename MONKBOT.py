import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
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

@client.command()
async def argument(ctx):
    await ctx.send("daarom  >:]")

@client.command(aliases=["F"])
async def f(ctx):
    await ctx.send("monke dead?")
    time.sleep(1)
    await ctx.send("monke sad.")

@client.command(aliases=["xd", "Xd", "xD"])
async def XD(ctx):
    await ctx.send("thats so fucking funny")

@client.command(aliases=["suggestion", "idea", "ideas"])
async def suggesties(ctx):
    await ctx.send("Stuur ideeën of suggesties naar @qweriop#0416.")

@client.command(aliases=["eten", "voedsel"])
async def food(ctx):
    await ctx.send(":banana:")

@client.command(aliases=["oorlog", "WAR"])
async def war(ctx):
    warRNG=random.randrange(1, 5)
    if warRNG==1:
        await ctx.send("MONKE KILLS THEM NAZIS!!")
    elif warRNG==2:
        await ctx.send("MONKE Killz all humanz on earth.")
    elif warRNG==3:
        await ctx.send("we monkes keel dem blooons!!!")
    else:
        await ctx.send("MONKE is launching nuuk on americ and ruski!!!")

client.run(TOKEN)