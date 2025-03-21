# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
from pulls import Anime, Manga

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
async def anime(ctx, *args):
    arguments = '%20'.join(args)
    if(len(args) == 0):
        await ctx.send("Please provide an anime title! (e.g. !anime Fruits Basket)")
    else:
        anime = Anime(arguments)

        embed = discord.Embed(
            color=discord.Color.brand_green(),
            description=anime.synopsis,
            title=anime.title,
            url = anime.url
        )
        embed.set_thumbnail(url = anime.image)
        embed.add_field(name = "⌛ Status", value = anime.status, inline=True)
        embed.add_field(name = "🗂️ Type", value = anime.type, inline=True)
        embed.add_field(name = "📅 Release", value = anime.dates, inline=False)
        if(anime.type != "movie"):
            embed.add_field(name = "💿 Total Episodes", value = anime.episodes, inline=True)
        if(anime.status == "finished" or anime.status == "current"):
            embed.add_field(name = "⭐ Average Rating", value = anime.rating, inline=True)
            embed.add_field(name = "🏆 Rank", value = anime.rank, inline=False)

        await ctx.send(embed=embed)

@bot.command()
async def manga(ctx, *args):
    arguments = '%20'.join(args)
    if(len(args) == 0):
        await ctx.send("Please provide an manga title! (e.g. !manga Fruits Basket)")
    else:
        manga = Manga(arguments)

        embed = discord.Embed(
            color=discord.Color.brand_green(),
            description=manga.synopsis,
            title=manga.title,
            url = manga.url
        )
        embed.set_thumbnail(url = manga.image)
        embed.add_field(name = "⌛ Status", value = manga.status, inline=True)
        embed.add_field(name = "🗂️ Type", value = manga.type, inline=True)
        embed.add_field(name = "📅 Release", value = manga.dates, inline=False)
        if(manga.status == "finished"):
            embed.add_field(name = "📚 Total Chapters", value = manga.chapters, inline=True)
            embed.add_field(name = "⭐ Average Rating", value = manga.rating, inline=True)
            embed.add_field(name = "🏆 Rank", value = manga.rank, inline=False)
        elif(manga.status == "current"):
            embed.add_field(name = "⭐ Average Rating", value = manga.rating, inline=True)
            embed.add_field(name = "🏆 Rank", value = manga.rank, inline=False)


        await ctx.send(embed=embed)
    
bot.run(token)
