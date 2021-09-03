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
        for data in soup.select(f'a[href*={query.lower()}]'):
            link_list.append(''.join([HOST, data['href']]))
            title_list.append(data.text)
        # shitty fix for some results that can't be included in the range(10)
        i = 0
        while i >= 10:
            res.append(structs.Song(link_list[i], provider="Soundcloud", title=title_list[i], album="WIP"))
        return res
