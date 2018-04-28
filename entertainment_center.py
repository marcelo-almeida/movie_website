import media
import fresh_tomatoes

MOVIE_TITLE_KEY = "movie_title"
MOVIE_STORYLINE_KEY = "movie_storyline"
POSTER_IMAGE_URL_KEY = "poster_image_url"
TRAILER_YOUTUBE_URL_KEY = "trailer_youtube_url"


def get_movies_information():
    movie_information_list = [
        {
            MOVIE_TITLE_KEY: "Avengers: Infinity War",
            MOVIE_STORYLINE_KEY:
                "A superhero film based on the Marvel Comics superhero team the Avengers",
            POSTER_IMAGE_URL_KEY:
                "https://upload.wikimedia.org/wikipedia/commons/4/45/Avengers_Infinity_War_logo_001.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=6ZfuNTqbHE8"
        },
        {
            MOVIE_TITLE_KEY: "Avengers: Infinity War",
            MOVIE_STORYLINE_KEY:
                "A superhero film based on the Marvel Comics superhero team the Avengers",
            POSTER_IMAGE_URL_KEY:
                "https://upload.wikimedia.org/wikipedia/commons/4/45/Avengers_Infinity_War_logo_001.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=6ZfuNTqbHE8"
        }
    ]
    return movie_information_list


def create_movie_trailer(movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
    movie = media.Movie(movie_title, movie_storyline, poster_image_url, trailer_youtube_url)
    return movie


def create_movie_list():
    movie_information_list = get_movies_information()
    movies = []
    for movie_information in movie_information_list:
        movie = create_movie_trailer(movie_information[MOVIE_TITLE_KEY],
                                     movie_information[MOVIE_STORYLINE_KEY],
                                     movie_information[POSTER_IMAGE_URL_KEY],
                                     movie_information[TRAILER_YOUTUBE_URL_KEY])
        movies.append(movie)
    return movies


def append_movies_to_the_view():
    movies = create_movie_list()
    fresh_tomatoes.open_movies_page(movies)


append_movies_to_the_view()
