from flask import Flask, flash, redirect, request, jsonify, json
import modules as md

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

@app.route('/downloadImage/<name>')
def downloadImage(name):
    url ="https://o.aolcdn.com/images/dims?quality=85&image_uri=https%3A%2F%2Fs.aolcdn.com%2Fhss%2Fstorage%2Fmidas%2Fdba1b71c87c7ef0d2ce3cd26dd1eb15e%2F206449491%2FMSM_Screen_PS4Pro_E32018_00003.jpg&client=amp-blogside-v2&signature=9a8deccbe35c8d1c98ebdc980ecc27abf926f761"
    md.downloadImage(url,name)
    return "got it"


def main():
    app.run(host='0.0.0.0', debug=True)
