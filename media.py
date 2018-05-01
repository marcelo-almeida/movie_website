class Video:
    """The class Video have the commons attributes and methods from video types

        Attributes:
            title (str): title of the video.
            extended_title (str): additional or extended title of the video, example: episode I
            duration (str): duration of the video
        Method:
            get_full_title (str): get title joined with extended_title
    """

    def __init__(self, title, extended_title, duration):
        self.title = title
        self.extended_title = extended_title
        self.duration = duration

    def get_full_title(self):
        return self.title + " " + self.extended_title


class Movie(Video):
    """The class Movie includes a inheritance with Video class and have specific attributes about Movies

        Attributes:
            movie_storyline (str): a little description about the movie.
            poster_image_url (str): url for image of the movie
            trailer_youtube_url (str): url for youtube trailer of the movie
    """

    def __init__(self, movie_title, movie_extended_title, movie_storyline,
                 poster_image_url, trailer_youtube_url, duration):
        Video.__init__(self, movie_title, movie_extended_title, duration)
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
