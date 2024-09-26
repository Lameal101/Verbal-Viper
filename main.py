from flask import Flask,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/") #python decorators
def hello_world():
    return "<h2>this website is working</h2>"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")