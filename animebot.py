# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def test(ctx, arg):
    await ctx.send("i going to blow up sunmilk's house :3")

@bot.command()
async def anime(ctx, *args):
    arguments = ' '.join(args)
    if(len(args) == 0):
        await ctx.send("Please provide an anime title! (e.g. !anime Fruits Basket)")
    
bot.run(token)
