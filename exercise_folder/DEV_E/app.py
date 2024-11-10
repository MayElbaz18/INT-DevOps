from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/calc', methods=['GET'])
def calc():
    try:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        operation = request.args.get('operation')

        if not num1 or not num2:
            return jsonify('Please enter two numbers'), 400
        

        num1 = float(num1)
        num2 = float(num2)
       

        if operation == 'add':
            result = num1 + num2

        elif operation == 'subtract':
            result = num1 - num2
            

        elif operation == 'multiply':
            result = num1 * num2 
            

        elif operation == 'divide':
            if num2 == 0:
                return jsonify("Cannot divide by zero."), 400
            result = num1 / num2 
            

        return jsonify({'Result': result})

    except ValueError:
        return jsonify("Please enter only numbers") , 400     


if __name__ == "__main__":
    app.run(port=8080, debug= True)