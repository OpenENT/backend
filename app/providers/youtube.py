from youtubesearchpython import *
from provider import Provider

import structs

class YoutubeProvider(Provider):

    def __init__(self):
        super().__init__(name='Youtube')

    def search(self, query: str): # TODO: download etc
        res = list()
        videosSearch = VideosSearch(query, 10)
        for i in range(videosSearch.limit): # kinda shitty
            res.append(structs.Song
            (videosSearch.result()["result"][i]["link"], 
            title=videosSearch.result()["result"][i]["title"], 
            album=structs.Album(
                img_url=videosSearch.result()["result"][i]["thumbnails"][0]["url"],
                artist=structs.Artist(name=videosSearch.result()["result"][i]["channel"]["name"]))))
        return res

        