import requests
import json
import os

# Open the config file
with open('Movie/config.json', 'r') as f:
    config = json.load(f)


# Create the file movie.json if isn't exist
if not os.path.exists('Movie/movie.json'):
    with open('Movie/movie.json', 'w') as f:
        f.write("{}")   

# Open movie.json to read data
with open('Movie/movie.json', 'r') as f:
 current_info = json.load(f)            

def movie_found_in_file(search): 
    if search in current_info:
        print(f'{search} is already in the movie.json file!')
        return True
    return False

# Geting movie from API databse
def get_movie(search):
    headers = {
	"x-rapidapi-key": config['key'],
	"x-rapidapi-host": config['host']
     }
    url = config['url']
    querystring = {"s":search}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json().get('Search', [])
    if data:
            print(f"Movies matching '{search}':")
            movie_list = {}  # Take all data from API

            # Loop through all movies in the search results and store title and year only
            for movie_data in data:
                title = movie_data.get('Title')
                year = movie_data.get('Year')
                
                # Print only the Title and Year
                print(f"Title: {title}, Year: {year}")

                # Store each movie's Title and Year in the dictionary inside the JSON file
                movie_list[title] = {'title': title, 'year': year}

            # Save the search results in the JSON file under the search key
            with open('Movie/movie.json', 'r') as f:
                    current_info = json.load(f)


            # Save the new search results under the search key
            current_info[search] = movie_list

            with open('Movie/movie.json', 'w') as f:
                json.dump(current_info, f, indent=4)
  

# Print movie information from the JSON file
def response(search):
    with open('Movie/movie.json', 'r') as f:
        current_info = json.load(f)
    if search in current_info:
        print(f"Movies found for '{search}' in the JSON file:")
        for movie, info in current_info[search].items():
            print(f"Title: {info['title']}, Year: {info['year']}")
    else:
        print(f'No information found for "{search}" in the local database!')

