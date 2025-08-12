class Song:
    count = 0
    genres = []           # All genres including duplicates
    artists = []          # All artists including duplicates
    unique_genres = []    # Unique genres only (optional)
    unique_artists = []   # Unique artists only (optional)
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()

        # Append all genres and artists (for counts)
        Song.genres.append(genre)
        Song.artists.append(artist)

        # Update unique lists (optional, depending on your requirements)
        self.add_to_genres()
        self.add_to_artists()

        # Update histograms
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        if cls.genres[-1] not in cls.unique_genres:
            cls.unique_genres.append(cls.genres[-1])

    @classmethod
    def add_to_artists(cls):
        if cls.artists[-1] not in cls.unique_artists:
            cls.unique_artists.append(cls.artists[-1])

    @classmethod
    def add_to_genre_count(cls):
        genre_histogram = {}
        for genre in cls.genres:
            genre_histogram[genre] = genre_histogram.get(genre, 0) + 1
        cls.genre_count = genre_histogram

    @classmethod
    def add_to_artist_count(cls):
        artist_histogram = {}
        for artist in cls.artists:
            artist_histogram[artist] = artist_histogram.get(artist, 0) + 1
        cls.artist_count = artist_histogram
