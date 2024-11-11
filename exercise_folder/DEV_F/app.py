from flask import Flask, render_template, jsonify, request
import re
import json
import os


app = Flask('__name__')


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/feedback', methods=['GET'])
def feedback():
    try:
        name = request.args.get('name')
        email = request.args.get('email')
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        feedback = request.args.get('feedback')
        message = 'Thank you for your feedback!'

        if not name or not email or not feedback:
            return jsonify('All fields are requierd for feedback'), 400
        
        if not re.match(email_regex, email):
            return jsonify('Please enter a valid email'), 400

        feedback_data = {
            "name": name,
            "email": email,
            "feedback": feedback
        }

        with open("feedback.txt", "a") as f:
            f.write(json.dumps(feedback_data) + "\n")        
        
        return jsonify({'Success': message}), 200    
    
    except Exception as e:
        return jsonify({'Error':f'error {e}'}), 500

if __name__ =="__main__":
    app.run(port=8080, debug=True)