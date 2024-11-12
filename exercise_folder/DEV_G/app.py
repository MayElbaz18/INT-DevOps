from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/count", methods=['GET'])
def count():
    words = request.args.get('words')
    word_count = len(words.split()) if words.strip() else 0

    return jsonify({"Number_Of_Words": word_count})

if __name__ == "__main__":
    app.run(port=8080, debug=True)