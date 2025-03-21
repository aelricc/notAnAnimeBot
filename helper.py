from pulls import Anime, Manga
import discord

#Need to clean this up it's so bad
def createEmbed(request):
    embed = discord.Embed(
        color=discord.Color.brand_green(),
        description=request.synopsis,
        title=request.title,
        url = request.url
    )
    embed.set_thumbnail(url = request.image)
    embed.add_field(name = "⌛ Status", value = request.status, inline=True)
    if(request.reqt != "movie"): embed.add_field(name = "🗂️ Type", value = request.type, inline=True)
    if(request.genres): embed.add_field(name = "🔖 Genres", value = request.genres, inline=False)
    embed.add_field(name = "📅 Release", value = request.dates, inline=False)
    if(request.reqt != "movie"): 
        if (request.type != "Movie"): embed.add_field(name = "💿 Total Episodes", value = request.episodes, inline=True)
        if (request.reqt == "tv"): embed.add_field(name = "💽 Total Seasons", value = request.seasons, inline=True)
        if (request.status == "Finished"): embed.add_field(name = "📚 Total Chapters", value = request.chapters, inline=True)
        embed.add_field(name = "⭐ Average Rating", value = request.rating, inline=True)
        if (request.reqt != "tv"): embed.add_field(name = "🏆 Rank", value = request.rank, inline=True)
    else: embed.add_field(name = "⭐ Average Rating", value = request.rating, inline=True)
    return embed