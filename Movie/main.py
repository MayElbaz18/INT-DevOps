import argparse
import movie


parser = argparse.ArgumentParser(description='Search for a movie in the database')
parser.add_argument("-s", "--search", type=str, required=True, help="Movie Name To Search.")
search = parser.parse_args().search


if movie.movie_found_in_file(search):
    movie.response(search)
else:
    print("Movie not found in local database. Fetching from API...")
    movie.get_movie(search)
