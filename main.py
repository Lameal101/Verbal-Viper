from flask import Flask,render_template,request
from flask_cors import CORS
from test import rapgenerator as rg

app = Flask(__name__)
CORS(app)

@app.route("/") #python decorators
def hello_world():
    return render_template("index.html")

@app.route("/data",methods = ["GET","POST"])
def data():
    if request.method == "POST":
        lyrics = "can not be fetched"
        try:
            lyrics = rg(request.form["title"])
            print("check this out")
        except:
            pass

        return f"<pre>{lyrics}</pre>"
    return "<h1>HEAD</h1>"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")