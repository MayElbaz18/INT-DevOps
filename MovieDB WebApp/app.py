from flask import Flask, request, render_template, jsonify, send_from_directory
import os
import json
import movie

# Create the file movie.json if isn't exist
if not os.path.exists('MovieDB WebApp/static/movie.json'):
    with open('MovieDB WebApp/static/movie.json', 'w') as f:
        f.write("{}")            

app = Flask(__name__)

@app.route('/<filename>', methods=['GET'])
def static_file(filename):

    return send_from_directory('static', filename)

@app.route('/get_movie', methods=['GET'])
def getmovie():
    """
    Route to fetch Movie information in text format based on 'search' query parameter.
    """
    search = request.args.get('search', default=None)
    with open('MovieDB WebApp/static/movie.json', 'r') as f:
     current_info = json.load(f) 

    if search in current_info:
       f'{search} is already in the movie.json file!'
       output = movie.response(search)
       return output

    if search not in current_info:
        movie.get_movie(search)
        output = movie.response(search)
        return output
    else:
        return 'No search provided!', 400
    


@app.route('/health', methods=['GET'])
def health():
    health = {}
    try:
      health['status'] = "OK"
    except Exception as e:
        return f"An error occurred: {e}"

    return jsonify(health)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)