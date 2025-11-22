from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/square', methods=['POST', 'GET'])
def square():
    # If a route has multiple methods, you can use if statements to split logic
    # Or, use multiple functions with the same route but different methods
    if request.method == 'GET':
        number = 2
        return {'result': int(number) ** 2}
    data = request.get_json()
    number = data.get('number', 0)
    return {'result': int(number) ** 2}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
