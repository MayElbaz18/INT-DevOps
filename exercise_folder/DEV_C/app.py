from flask import Flask, render_template, jsonify, request
import requests
import re


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/URL_liveness", methods=['GET'])
def URL_liveness():
    url = request.args.get('url')

    if not url.startswith(('http://', 'https://')):
        url = f'http://{url}'

    # -----  validation to check that the URL format includes a top-level domain ----- #
    if not re.match(r'^(https?://)?[^\s/]+\.[a-zA-Z]{2,}$', url):
        return jsonify({'status_code': 'INVAILD_FORMAT'})
    
    try:
        response = requests.get(url, timeout=1)

        if response.status_code == 200:
            return jsonify({'status_code': 'LIVE'})
        
        else:
            return jsonify({'status_code': 'UNREACHABLE'})
        
    except requests.exceptions.RequestException:
        return jsonify({'status_code': 'UNREACHABLE'})

if __name__ == "__main__":
    app.run(port=8080, debug=True)
