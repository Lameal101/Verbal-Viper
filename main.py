from flask import Flask,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/") #python decorators
def hello_world():
    return "<h2>this website is working</h2>"

@app.route("/red")
def tomatos():
    return render_template("index.html")

@app.route("/iron")
def fan():
    return "<h3>fans and breezes</h3>"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")