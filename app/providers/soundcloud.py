from bs4 import BeautifulSoup
from pathlib import Path
from provider import Provider

import requests
import structs
import subprocess

HOST = "https://soundcloud.com"

class SoundcloudProvider(Provider):

    def __init__(self):
        super().__init__(name='Soundcloud')
    
    def search(self, query: str):
        res = list()
        req = requests.get(f"{HOST}/search?q={query.replace('+', '%20')}")
        soup =  BeautifulSoup(req.content, 'html.parser')
        dikt = dict()
        query = query.replace(' ', '-').replace("'", "")
        try:
            for data in soup.select(f'a[href*={query.lower()}]'):
                dikt[''.join([HOST, data['href']])] = data.text
            for url, title in dikt.items():
                res.append(structs.Song(url, provider=self.name, title=title))
        except Exception as e:
            print(e)
        return res
    
    def download(self, stream_url: str):
        id = stream_url[23:].replace('/', '-')
        file_path = Path(f'streams/{id}.opus')
        if file_path.is_file():
            return f'{id}.opus'
        else:
            command = f"yt-dlp --output streams/{id}.%\(ext\)s -f hls_opus_64 --embed-metadata --embed-thumbnail {stream_url}"
            process = subprocess.Popen(command, shell=True)
            process.wait()
            return f'{id}.opus'
