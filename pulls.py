
import requests, json

url = "https://api.jikan.moe/v4/"

class Request():
    def __init__(self, query, type):
        self.data = ((requests.get(f"{url}{type}/?q={query}&limit=1")).json())["data"][0]
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

class Anime(Request):
    def __init__(self, query):
        super().__init__(query, "anime")
        self.dates = str(self.data["aired"]["string"])
        self.episodes = str(self.data["episodes"])

class Manga(Request):
    def __init__(self, query):
        super().__init__(query, "manga")
        self.dates = str(self.data["published"]["string"])
        self.chapters = str(self.data["chapters"])