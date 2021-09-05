from bs4 import BeautifulSoup
from provider import Provider
import structs
import subprocess
import requests

HOST = "https://soundcloud.com"

class SoundcloudProvider(Provider):
    def __init__(self):
        super().__init__(name='Soundcloud')
    
    def search(self, query: str):
        res = list()
        req = requests.get(f"{HOST}/search?q={query.replace('+', '%20')}")
        soup =  BeautifulSoup(req.content, 'html.parser')
        # seems weird but it works
        link_list = list()
        title_list = list()
        query = query.replace(' ', '-')
        query = query.replace("'", "")
        try:
            for data in soup.select(f'a[href*={query.lower()}]'):
                link_list.append(''.join([HOST, data['href']]))
                title_list.append(data.text)
            for i in range(len(link_list[:10])):
                res.append(structs.Song(link_list[i], provider="Soundcloud", title=title_list[i], album="WIP"))
        except:
            pass
        return res
    
    def download(self, stream_url: str):
        id = stream_url[23:]
        id = id.replace('/', '-')
        command = f"yt-dlp --output streams/{id}.%\(ext\)s -f hls_opus_64 --embed-metadata --embed-thumbnail {stream_url}"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        return f'{id}.opus'
