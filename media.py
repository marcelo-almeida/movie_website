import webbrowser


class Movie:
    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_youtube_url):
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youTube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)