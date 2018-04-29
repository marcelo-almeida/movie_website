class Video:
    def __init__(self, title, extended_title, duration):
        self.title = title
        self.extended_title = extended_title
        self.duration = duration

    def get_full_title(self):
        return self.title + " " + self.extended_title


class Movie(Video):
    def __init__(self, movie_title, movie_extended_title, movie_storyline,
                 poster_image_url, trailer_youtube_url, duration):
        Video.__init__(self, movie_title, movie_extended_title, duration)
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
