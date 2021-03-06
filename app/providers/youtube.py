from pathlib import Path
from provider import Provider
from youtubesearchpython import VideosSearch
import structs
import subprocess

class YoutubeProvider(Provider):

    def __init__(self):
        super().__init__(name='Youtube')

    def search(self, query: str): # TODO: download etc
        res = list()
        videosSearch = VideosSearch(query, 10)
        for i in range(videosSearch.limit): # kinda shitty
            res.append(structs.Song(
                videosSearch.result()["result"][i]["link"], 
                provider=self.name,
                title=videosSearch.result()["result"][i]["title"],
                album=structs.Album(
                    img_url=videosSearch.result()["result"][i]["thumbnails"][0]["url"],
                    artist=structs.Artist(name=videosSearch.result()["result"][i]["channel"]["name"]))))
        return res

    def download(self, stream_url: str):
        id = stream_url[31:]
        file_path = Path(f'streams/{id}.opus')
        if file_path.is_file():
            return f'{id}.opus'
        else:
            command = f"yt-dlp --output streams/{id}.%\(ext\)s -x -f bestaudio --embed-metadata --embed-thumbnail {stream_url}"
            process = subprocess.Popen(command, shell=True)
            process.wait()
            return f'{id}.opus'
        
