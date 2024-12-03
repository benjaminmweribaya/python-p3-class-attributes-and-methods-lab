class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
        return

    def __str__(self):
        return f"{self.name} by {self.artist} ({self.genre})"
    
    def __repr__(self):
        return f"{self.name} by {self.artist} ({self.genre})"
    
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
        return

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
        return

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
        return

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
        return
    
    def __eq__(self, other):
        if self.name == other.name and self.artist == other.artist and self.genre == other.genre:
            return True
        else:
            return False
        return

    def __hash__(self):
        return hash((self.name, self.artist, self.genre))   
        
        
