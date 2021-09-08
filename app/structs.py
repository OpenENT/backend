
def Artist(name="Unknown", img_url=None, tags=None):
    return {"type": "artist", "name": name, "img_url": img_url, "tags": tags}

def Album(title="Unknown", img_url=None, tags=None, artist=Artist()):
    return {"type": "album", "title": title, "img_url": img_url, "artist": artist, "tags": tags}

def Song(stream_url, provider, title="Unknown", album=Album()):
    return {"type": "song", "title": title, "stream_url": stream_url, "provider": provider, "album": album}
