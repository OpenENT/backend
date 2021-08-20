
def Artist(name="Unknown", img_url=None, tags=None):
    return {"name": name, "img_url": img_url, "tags": tags}

def Album(title="Unknown", img_url=None, tags=None, artist=Artist()):
    return {"title": title, "img_url": img_url, "artist": artist, "tags": tags}

def Song(stream_url, title="Unknown", album=Album()):
    return {"title": title, "stream_url": stream_url, "album": album}