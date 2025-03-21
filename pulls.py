
import requests, json

k_url = "https://kitsu.io/api/edge"
headers = {
    'Accept': 'application/vnd.api+json',
    'Content-Type': 'application/vnd.api+json'
}

class Anime:
    def __init__(self, title):
        self.data = (requests.get(k_url + "/anime?filter[text]=" + title, headers=headers)).json()
        self.title = str(self.data["data"][0]["attributes"]["canonicalTitle"])
        self.image = str(self.data["data"][0]["attributes"]["posterImage"]["medium"])
        self.synopsis = str(self.data["data"][0]["attributes"]["synopsis"])
        self.url = "https://kitsu.app/anime/" + str(self.data["data"][0]["id"])
        self.type = str(self.data["data"][0]["attributes"]["subtype"])
        self.status = str(self.data["data"][0]["attributes"]["status"])
        if self.type != "movie":
            self.dates = str(self.data["data"][0]["attributes"]["startDate"]) + " to " + str(self.data["data"][0]["attributes"]["endDate"])
            self.episodes = str(self.data["data"][0]["attributes"]["episodeCount"])
        else:
            self.dates = str(self.data["data"][0]["attributes"]["startDate"])
        if (self.status == "current" or self.status == "finished"):
            self.rating = str(self.data["data"][0]["attributes"]["averageRating"]) + "/100"
            self.rank = str(self.data["data"][0]["attributes"]["popularityRank"])


class Manga:
    def __init__(self, title):
        self.data = (requests.get(k_url + "/manga?filter[text]=" + title, headers=headers)).json()
        self.title = str(self.data["data"][0]["attributes"]["canonicalTitle"])
        self.image = str(self.data["data"][0]["attributes"]["posterImage"]["medium"])
        self.synopsis = str(self.data["data"][0]["attributes"]["synopsis"])
        self.url = "https://kitsu.app/manga/" + str(self.data["data"][0]["id"])
        self.type = str(self.data["data"][0]["attributes"]["subtype"])
        self.status = str(self.data["data"][0]["attributes"]["status"])
        if self.status == "finished":
            self.dates = str(self.data["data"][0]["attributes"]["startDate"]) + " to " + str(self.data["data"][0]["attributes"]["endDate"])
            self.chapters = str(self.data["data"][0]["attributes"]["chapterCount"])
        else:
            self.dates = str(self.data["data"][0]["attributes"]["startDate"])
        if (self.status == "current" or self.status == "finished"):
            self.rating = str(self.data["data"][0]["attributes"]["averageRating"]) + "/100"
            self.rank = str(self.data["data"][0]["attributes"]["popularityRank"])