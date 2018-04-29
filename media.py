class Movie:
    def __init__(self, movie_title, movie_sequence_title, movie_storyline,
                 poster_image_url, trailer_youtube_url, duration):
        self.movie_title = movie_title
        self.movie_sequence_title = movie_sequence_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.duration = duration

    def get_full_title(self):
        return self.movie_title + " " + self.movie_sequence_title
