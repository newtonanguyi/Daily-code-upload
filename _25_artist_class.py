class Artist:
    def __init__(self, name, genre, number_of_albums):
        self.name = name
        self.genre = genre
        self.number_of_albums = number_of_albums

class Song(Artist):
    def __init__(self, name, genre, number_of_albums, title, duration=None):
        super().__init__(name, genre, number_of_albums)
        self.title = title
        self.duration = duration if duration else 'Unknown'

    def add_song(self, title, duration=None):
        self.title = title
        self.duaration = duration if duration else 'Unknown'

    def display_song_info(self):
        print(f"Song Title: {self.title}\nARtist: {self.name}\n(Genre: {self.genre}, Albums: {self.number_of_albums})\nDuration: {self.duration}")



song1 = Song('The Weekend', 'Pop', 10, 'Blinding Lights', '3:55')
song2 = Song('Drake', 'Hip Pop', 6, 'God\'s Plan', '4:45')
song1.add_song('Save your tears', '3:00')
song2.add_song('Blinding Lights', '3:55')
song1.add_song('Blinding Lights', '3:55')

song1.display_song_info()
song2.display_song_info()

