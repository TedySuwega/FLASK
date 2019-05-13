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
    url ="https://www.google.com/imgres?imgurl=https%3A%2F%2Fvignette.wikia.nocookie.net%2Fthedailybugle%2Fimages%2F2%2F2b%2FUltimate_Spider_Man_Render.png%2Frevision%2Flatest%3Fcb%3D20160319202253&imgrefurl=https%3A%2F%2Fthedailybugle.fandom.com%2Fwiki%2FSpider-Man&docid=I1FFzCCnUAsXMM&tbnid=1SMQP1XEsdMgCM%3A&vet=10ahUKEwjj6pmDuJjiAhVU8HMBHdTFBXsQMwiQASgZMBk..i&w=1778&h=2700&safe=strict&bih=969&biw=1920&q=spiderman&ved=0ahUKEwjj6pmDuJjiAhVU8HMBHdTFBXsQMwiQASgZMBk&iact=mrc&uact=8"
    md.downloadImage(url,name)
    return "got it"


def main():
    app.run(host='0.0.0.0', debug=True)
