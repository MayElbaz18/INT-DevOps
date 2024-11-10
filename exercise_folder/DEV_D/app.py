from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/temp_convertor', methods=['GET'])
def temp_convertor():
    try:
        temp = request.args.get('temp')
        if not temp:
            return jsonify('TEMPARTURE Is Missing!'), 400

        tempC = int(temp)
        convert = (tempC * 1.8) + 32

        return jsonify({'converted_temp': convert})

    except ValueError:
        return jsonify('TEMPARTURE Most Be A Number!'), 400


if __name__ == "__main__":
    app.run(port=8080, debug= True)
