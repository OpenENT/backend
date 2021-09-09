from pathlib import Path
from provider import Provider

import json
import requests
import structs
import subprocess

HOST = "https://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search"

class NicoProvider(Provider):

    def __init__(self):
        super().__init__(name="Nicovideo")

    def search(self, query: str):
        res = list()
        req = requests.get(f"{HOST}?q={query}&targets=title,tags&fields=contentId,title,tags,thumbnailUrl&_sort=-viewCounter&_offset=0&_limit=10&_context=niconico")
        content = json.loads(req.content)
        
        for i in range(len(content["data"])):
            id = content["data"][i]["contentId"]
            title = content["data"][i]["title"] 
            tags = content["data"][i]["tags"]
            thumbnail = content["data"][i]["thumbnailUrl"]
            artist = structs.Artist()
            album = structs.Album(title=title)
            song = structs.Song("https://nicovideo.jp/watch/"+id, provider=self.name, title=title, album=album)
            res.append(song)
        return res

    def download(self, stream_url: str):
        id = stream_url[30:]
        file_path = Path(f'streams/{id}.m4a')
        if file_path.is_file():
            return f'{id}.m4a'
        else:
            command = f"yt-dlp --output streams/{id}.%\(ext\)s -x --embed-metadata --embed-thumbnail {stream_url}"
            process = subprocess.Popen(command, shell=True)
            process.wait()
            return f'{id}.m4a'