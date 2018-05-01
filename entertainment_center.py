import media
import fresh_tomatoes

MOVIE_TITLE_KEY = "movie_title"
MOVIE_EXTENDED_TITLE_KEY = "movie_extended_title"
MOVIE_STORYLINE_KEY = "movie_storyline"
POSTER_IMAGE_URL_KEY = "poster_image_url"
TRAILER_YOUTUBE_URL_KEY = "trailer_youtube_url"
DURATION_KEY = "duration"


def get_movies_information():
    # create a list of map with movie information
    movie_information_list = [
        {
            MOVIE_TITLE_KEY: "The Lord of the Rings",
            MOVIE_EXTENDED_TITLE_KEY: "The Fellowship of the Ring",
            MOVIE_STORYLINE_KEY:
                "The beginning of the journey to destroy the one ring",
            POSTER_IMAGE_URL_KEY:
                "http://www-images.theonering.org/torwp/wp-content/uploads/2008/11/fellowship-movie-poster.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=zIu2hTgqquw",
            DURATION_KEY: "3h 48m"
        },
        {
            MOVIE_TITLE_KEY: "Doctor Strange",
            MOVIE_EXTENDED_TITLE_KEY: "",
            MOVIE_STORYLINE_KEY:
                "After a car accident a men lost of the use of his hands, but he find a way with mysterious magic.",
            POSTER_IMAGE_URL_KEY:
                "http://posterposse.com/wp-content/uploads/2016/10/Doctor-Strange-Poster-Marvel-Official.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=Lt-U_t2pUHI",
            DURATION_KEY: "1h 55m"
        },
        {
            MOVIE_TITLE_KEY: "Harry Potter",
            MOVIE_EXTENDED_TITLE_KEY: "and Philosopher's Stone",
            MOVIE_STORYLINE_KEY:
                "The beginning of the adventures of Harry Potter in the world of magic",
            POSTER_IMAGE_URL_KEY:
                "http://harrypotterfanzone.com/wp-content/2015/07/philosophers-stone-theatrical-poster.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=PbdM1db3JbY",
            DURATION_KEY: "2h 39m"
        },
        {
            MOVIE_TITLE_KEY: "Hobbit",
            MOVIE_EXTENDED_TITLE_KEY: "an Unexpected Journey",
            MOVIE_STORYLINE_KEY:
                "A journey of a hobbit and a group of dwarves to reclaim the kingdom of Erebor.",
            POSTER_IMAGE_URL_KEY:
                "http://concertposter.org/-2012Dec/Hobbit-MainArt-drop.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=SDnYMbYB-nU",
            DURATION_KEY: "3h 2m"
        },
        {
            MOVIE_TITLE_KEY: "Rogue One",
            MOVIE_EXTENDED_TITLE_KEY: "a Star Wars Story",
            MOVIE_STORYLINE_KEY:
                "A story about the theft of space station plans for the Rebel Alliance.",
            POSTER_IMAGE_URL_KEY:
                "https://vignette.wikia.nocookie.net/starwars/images/f/f5/"
                "Rogue_One_A_Star_Wars_Story_theatrical_poster.png",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=frdj1zb9sMY",
            DURATION_KEY: "2h 13m"
        },
        {
            MOVIE_TITLE_KEY: "Matrix",
            MOVIE_EXTENDED_TITLE_KEY: "",
            MOVIE_STORYLINE_KEY:
                "A story about Neo and the prophecy of the chosen one",
            POSTER_IMAGE_URL_KEY:
                "http://www.fatmovieguy.com/wp-content/uploads/2014/12/The-Matrix-Movie-Poster.jpg",
            TRAILER_YOUTUBE_URL_KEY: "https://www.youtube.com/watch?v=m8e-FF8MsqU",
            DURATION_KEY: "2h 16m"
        }
    ]
    return movie_information_list


def create_movie_trailer(movie_title,
                         movie_extended_title,
                         movie_storyline,
                         poster_image_url,
                         trailer_youtube_url,
                         duration):
    # create a instance of movie
    movie = media.Movie(movie_title,
                        movie_extended_title,
                        movie_storyline,
                        poster_image_url,
                        trailer_youtube_url,
                        duration)
    return movie


def create_movie_list():
    movie_information_list = get_movies_information()
    movies = []
    # for each movie_information create a instance of Movie and append in to list
    for movie_information in movie_information_list:
        movie = create_movie_trailer(movie_information[MOVIE_TITLE_KEY],
                                     movie_information[MOVIE_EXTENDED_TITLE_KEY],
                                     movie_information[MOVIE_STORYLINE_KEY],
                                     movie_information[POSTER_IMAGE_URL_KEY],
                                     movie_information[TRAILER_YOUTUBE_URL_KEY],
                                     movie_information[DURATION_KEY])
        movies.append(movie)
    return movies


def append_movies_to_the_view():
    movies = create_movie_list()
    # create the page with movies
    fresh_tomatoes.open_movies_page(movies)


append_movies_to_the_view()
