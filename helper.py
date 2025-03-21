from pulls import Anime, Manga
import discord

def createEmbed(request):
    embed = discord.Embed(
        color=discord.Color.brand_green(),
        description=request.synopsis,
        title=request.title,
        url = request.url
    )
    embed.set_thumbnail(url = request.image)
    embed.add_field(name = "⌛ Status", value = request.status, inline=True)
    embed.add_field(name = "🗂️ Type", value = request.type, inline=True)
    embed.add_field(name = "🔖 Genres", value = request.genres, inline=False)
    embed.add_field(name = "📅 Release", value = request.dates, inline=False)
    if ("Airing" in request.status):
        if (request.type != "Movie"): embed.add_field(name = "💿 Total Episodes", value = request.episodes, inline=True)
        embed.add_field(name = "⭐ Average Rating", value = request.rating, inline=True)
        embed.add_field(name = "🏆 Rank", value = request.rank, inline=True)
    elif ("Publishing" or "Finished" in request.status):
        if (request.status == "Finished"): embed.add_field(name = "📚 Total Chapters", value = request.chapters, inline=True)
        embed.add_field(name = "⭐ Average Rating", value = request.rating, inline=True)
        embed.add_field(name = "🏆 Rank", value = request.rank, inline=True)
        
    return embed