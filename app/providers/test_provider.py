from provider import Provider
import structs

class Test_Provider(Provider):

    def __init__(self):
        super().__init__(name='Test')

    def search(self, query: str):
        artist = structs.Artist(name="PinocchioP", img_url="https://static.wikia.nocookie.net/vocaloid/images/d/d0/PinocchioDoushite.jpg/revision/latest?cb=20210705085920")
        album = structs.Album(title="Human", img_url="https://static.wikia.nocookie.net/vocaloid/images/0/07/Human.jpg/revision/latest?cb=20170706215339", artist=artist)
        song = structs.Song("http://127.0.0.1:5000/usorasera.mp3", title="ウソラセラ", album=album)
        return (artist, album, song, song, song)