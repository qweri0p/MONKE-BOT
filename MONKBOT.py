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

@client.command(aliases=["monke", "MONKE", "monk", "MONK"])
async def MONKe(ctx):
    await ctx.send("MONKE")

@client.command()
async def update(ctx):
    await ctx.send("doin tha git pull")
    os.system("git pull")
    exit()

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
    await ctx.send("@qweriop#0416.")

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
        await ctx.send("us dart monkes keel dem blooons!!!")
    else:
        await ctx.send("MONKE is launching nuuk on americ and ruski!!!")


@client.command(aliases=["tellen", "counting"])
async def count(ctx):
    await ctx.send("Count Start!")
    for i in range(21):
        time.sleep(1.5)
        await ctx.send(i)
    time.sleep(1.5)
    await ctx.send("monke can't count further, monke is proud.")

@client.command(aliases=["monkbot", "ape"])
async def monkebot(ctx):
    await ctx.send("THATS MEEE!!!!")

client.run(TOKEN)
