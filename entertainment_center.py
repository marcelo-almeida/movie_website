import media
import fresh_tomatoes

MOVIE_TITLE_KEY = "movie_title"
MOVIE_STORYLINE_KEY = "movie_storyline"
POSTER_IMAGE_URL_KEY = "poster_image_url"
TRAILER_YOUTUBE_URL_KEY = "trailer_youtube_url"


def get_movies_information():
    movie_information_list = [
        {
            MOVIE_TITLE_KEY: "The Lord of the Rings",
            MOVIE_STORYLINE_KEY:
                "The beginning of the journey to destroy the one ring",
            POSTER_IMAGE_URL_KEY:
                "http://www-images.theonering.org/torwp/wp-content/uploads/2008/11/fellowship-movie-poster.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=V75dMMIW2B4"
        },
        {
            MOVIE_TITLE_KEY: "Doctor Strange",
            MOVIE_STORYLINE_KEY:
                "After a car accident a men lost of the use of his hands, but he find a way with mysterious magic.",
            POSTER_IMAGE_URL_KEY:
                "http://posterposse.com/wp-content/uploads/2016/10/Doctor-Strange-Poster-Marvel-Official.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=Lt-U_t2pUHI"
        },
        {
            MOVIE_TITLE_KEY: "Harry Potter",
            MOVIE_STORYLINE_KEY:
                "The beginning of the adventures of Harry Potter in the world of magic",
            POSTER_IMAGE_URL_KEY:
                "http://harrypotterfanzone.com/wp-content/2015/07/philosophers-stone-theatrical-poster.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=PbdM1db3JbY"
        },
        {
            MOVIE_TITLE_KEY: "Hobbit",
            MOVIE_STORYLINE_KEY:
                "A journey of a hobbit and a group of dwarves to reclaim the kingdom of Erebor.",
            POSTER_IMAGE_URL_KEY:
                "http://concertposter.org/-2012Dec/Hobbit-MainArt-drop.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=SDnYMbYB-nU"
        },
        {
            MOVIE_TITLE_KEY: "Rogue One",
            MOVIE_STORYLINE_KEY:
                "A story about the theft of space station plans for the Rebel Alliance.",
            POSTER_IMAGE_URL_KEY:
                "https://vignette.wikia.nocookie.net/starwars/images/f/f5/Rogue_One_A_Star_Wars_Story_theatrical_poster.png",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=frdj1zb9sMY"
        },
        {
            MOVIE_TITLE_KEY: "Matrix",
            MOVIE_STORYLINE_KEY:
                "A story about Neo and the prophecy of the chosen one",
            POSTER_IMAGE_URL_KEY:
                "http://www.fatmovieguy.com/wp-content/uploads/2014/12/The-Matrix-Movie-Poster.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=m8e-FF8MsqU"
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
