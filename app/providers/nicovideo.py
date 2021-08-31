from provider import Provider

import subprocess
import requests
import structs
import json

HOST = "https://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search"

class NicoProvider(Provider):

    def __init__(self):
        super().__init__(name="Nicovideo")


    def search(self, query: str): # TODO: download etc
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
            song = structs.Song("https://nicovideo.com/watch/"+id, title=title, album=album)
            res.append(song)
        return res

    def download(self, stream_url: str):
        id = stream_url[31:]
        command = f"yt-dlp --output streams/{id}.%\(ext\)s -x -f h264_300kbps_360p-aac_64kbps {stream_url}"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        return f'{id}.m4a'