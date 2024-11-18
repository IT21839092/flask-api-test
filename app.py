from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    return jsonify({'result': num1 + num2})

if __name__ == '__main__':
    app.run(debug=True)
