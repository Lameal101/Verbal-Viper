from flask import Flask,render_template,request
from flask_cors import CORS
from test import rapgenerator as rg

app = Flask(__name__)
CORS(app)

@app.route("/") #python decorators
def hello_world():
    return "<h2>this website is working</h2>"

@app.route("/data",methods = ["GET","POST"])
def data():
    if request.method == "POST":
        print(request.json)
        print(request.json["title"])
        lyrics = rg(request.json["title"])
        return lyrics
    return "<h1>HEAD</h1>"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")