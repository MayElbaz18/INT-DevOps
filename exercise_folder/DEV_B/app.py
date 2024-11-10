from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/URL_liveness", methods=['GET'])
def URL_liveness():
    url = request.args.get('url')
    try:
        response = requests.get(f'http://{url}', timeout=1)
        
        if response.status_code == 200:
            return {'status_code': 'LIVE'}
        
        else:
            return {'status_code': 'UNREACHABLE'}
        
    except requests.exceptions.RequestException:
    
        return {'status_code': 'UNREACHABLE'}

if __name__ == "__main__":
    app.run(port=8080, debug=True)
