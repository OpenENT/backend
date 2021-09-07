from provider import Provider
import structs

from pathlib import Path
import re
import mutagen

class LocalProvider(Provider):
    def __init__(self):
        super().__init__(name='Local')
    
    def search(self, query: str):
        formats = (".flac", ".mp3", ".m4a", ".aac", ".ape", ".wav", ".aiff", ".opus", ".mpc", ".ogg", ".wma")
        path = Path('PATH TO INSERT')
        res = list()
        for file in path.rglob(f"*.*"):
            if re.search(query, file.name, re.IGNORECASE):
                if str(file).endswith(formats):
                    metadata = mutagen.File(file)
                    res.append(structs.Song(str(file), provider=self.name, title=metadata['title'][0], album=metadata['album'][0]))
        return res