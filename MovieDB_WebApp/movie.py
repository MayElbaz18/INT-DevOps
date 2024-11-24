import requests
import json
import os

# Open the config file
with open('MovieDB WebApp/static/config.json', 'r') as f:
    config = json.load(f)

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
            with open('MovieDB WebApp/static/movie.json', 'r') as f:
                    current_info = json.load(f)


            # Save the new search results under the search key
            current_info[search] = movie_list

            with open('MovieDB WebApp/static/movie.json', 'w') as f:
                json.dump(current_info, f, indent=4)
  

# Print movie information from the JSON file
def response(search):
    output = ""
    with open('MovieDB WebApp/static/movie.json', 'r') as f:
        current_info = json.load(f)
    if search in current_info:
        for search, info in current_info[search].items():
            output += f"Title: {info['title']}, Year: {info['year']}\n"
    elif search not in current_info:
        output += f'No information found for "{search}" in the local database!\n'
    
    return output

