import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
from pulls import Anime, Manga, Movie, TV
from helper import createEmbed

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
    if(arg == "emergencyprotocol"):
        await ctx.send("i going to blow up sunmilk's house :3")
    else:
        await ctx.send("hi :3")

@bot.command()
async def apologize(ctx, arg1, arg2):
    await ctx.send("im sorry " + str(arg2) + " :(")

@bot.command()
async def execute(ctx, *args):
    arguments = '%20'.join(args)
    if(len(args) != 0):
        await ctx.send("Command recieved. Executing orders.")

@bot.command()
async def anime(ctx, *args):
    arguments = '%20'.join(args)
    if(len(args) == 0):
        await ctx.send("Please provide an anime title! (e.g. !anime Fruits Basket)")
    else:
        try: 
            anime = Anime(arguments)
            embed = createEmbed(anime)
            print(f"Found anime for query {arguments}")
            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send("sorry, i couldn't find that anime :(")

@bot.command()
async def manga(ctx, *args):
    arguments = '%20'.join(args)
    if(len(args) == 0):
        await ctx.send("Please provide an manga title! (e.g. !manga Fruits Basket)")
    else:
        try: 
            manga = Manga(arguments)
            embed = createEmbed(manga)
            print(f"Found manga for query {arguments}")
            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send("sorry, i couldn't find that manga :(")

@bot.command()
async def movie(ctx, *args):
    arguments = ' '.join(args)
    if(len(args) == 0):
        await ctx.send("Please provide a movie title! (e.g. !movie Inception)")
    else:
        try:
            movie = Movie(arguments)
            embed = createEmbed(movie)
            print(f"Found movie for query {arguments}")
            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send("sorry, i couldn't find that movie :(")
        
@bot.command()
async def tv(ctx, *args):
    arguments = ' '.join(args)
    if(len(args) == 0):
        await ctx.send("Please provide a TV show title! (e.g. !tv Inception)")
    else:
        try: 
            tv = TV(arguments)
            embed = createEmbed(tv)
            print(f"Found TV for query {arguments}")
            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send("sorry, i couldn't find that show :(")

bot.run(token)
