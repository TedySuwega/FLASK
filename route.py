from flask import Flask, flash, redirect, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/hello', methods=['GET'])
def hello():
    print('hello')

@app.route('/hello/<name>', methods=['GET'])
def say_name(name):
    print('hai',name)

def main():
    app.run(host='0.0.0.0', debug=True)
