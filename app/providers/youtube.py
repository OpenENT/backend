from youtubesearchpython import VideosSearch
from provider import Provider
import subprocess
import structs

class YoutubeProvider(Provider):

    def __init__(self):
        super().__init__(name='Youtube')

    def search(self, query: str): # TODO: download etc
        res = list()
        videosSearch = VideosSearch(query, 10)
        for i in range(videosSearch.limit): # kinda shitty
            res.append(structs.Song(
                videosSearch.result()["result"][i]["link"], 
                provider="YouTube",
                title=videosSearch.result()["result"][i]["title"],
                album=structs.Album(
                    img_url=videosSearch.result()["result"][i]["thumbnails"][0]["url"],
                    artist=structs.Artist(name=videosSearch.result()["result"][i]["channel"]["name"]))))
        return res

    def download(self, stream_url: str):
        id = stream_url[31:]
        command = f"yt-dlp --output streams/{id}.%\(ext\)s -x -f bestaudio {stream_url}"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        return f'{id}.opus'
        