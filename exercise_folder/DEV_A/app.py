from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/get_time", methods=['GET'])
def get_time():
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return jsonify(time=current_time)


if __name__ == "__main__":
    app.run(port=8080, debug=True)


