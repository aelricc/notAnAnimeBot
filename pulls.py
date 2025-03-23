import os
import requests, json

jurl = "https://api.jikan.moe/v4/"
murl = "https://api.themoviedb.org/3/"
mheaders = {
    "accept": "application/json",
    "Authorization": "Bearer " + os.getenv("TMDB_TOKEN")
}

class malRequest():
    def __init__(self, query, type):
        self.data = ((requests.get(f"{jurl}{type}/?q={query}&limit=1")).json())["data"][0]
        self.title = str(self.data["title"])
        self.image = str(self.data["images"]["jpg"]["large_image_url"])
        self.synopsis = str(self.data["synopsis"])
        self.url = str(self.data["url"])
        self.type = str(self.data["type"])
        self.status = str(self.data["status"])
        self.rating = str(self.data["score"])
        self.rank = str(self.data["rank"])
        genres = [d.get("name") for d in self.data["genres"] if "name" in d]
        self.genres = ", ".join(genres)
        self.reqt = type

class Anime(malRequest):
    def __init__(self, query):
        super().__init__(query, "anime")
        self.dates = str(self.data["aired"]["string"])
        self.episodes = str(self.data["episodes"])

class Manga(malRequest):
    def __init__(self, query):
        super().__init__(query, "manga")
        self.dates = str(self.data["published"]["string"])
        self.chapters = str(self.data["chapters"])
    
class tmdbRequest():
    def __init__(self, query, type):
        response = requests.get(f"{murl}search/{type}?query={query}&include_adult=false&language=en-US&page=1", headers=mheaders)
        self.data = requests.get(f"{murl}{type}/{response.json()["results"][0]["id"]}?language=en-US", headers = mheaders).json()
        self.image = str(f"https://image.tmdb.org/t/p/original{self.data["poster_path"]}")
        self.synopsis = str(self.data["overview"])
        self.url = str(self.data["homepage"])
        self.status = str(self.data["status"])
        self.rating = str(int(self.data["vote_average"]*10))
        genres = [d.get("name") for d in self.data["genres"] if "name" in d]
        self.genres = ", ".join(genres)
        self.rank = None
        self.reqt = type

class Movie(tmdbRequest):
    def __init__(self, query):
        super().__init__(query, "movie")
        self.title = str(self.data["title"])
        self.dates = str(self.data["release_date"])

class TV(tmdbRequest):
    def __init__(self, query):
        super().__init__(query, "tv")
        self.title = str(self.data["name"])
        self.episodes = str(self.data["number_of_episodes"])
        self.seasons = str(self.data["number_of_seasons"])
        self.dates = str(f"{self.data["first_air_date"]} to {self.data["last_air_date"]}")
        self.type = str(self.data["type"])