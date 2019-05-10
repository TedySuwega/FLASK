from flask import Flask, flash, redirect, request, jsonify, json

app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'

@app.route('/hello/<name>', methods=['GET'])
def say_name(name):
    return ('<h1>hai '+ name+'<h1>')

@app.route('/helloJson/<name>')
def say_name_json(name):
    Nama = {'name': name}
    result = json.dumps(Nama)
    return result

def main():
    app.run(host='0.0.0.0', debug=True)
