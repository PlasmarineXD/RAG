from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["GET","POST"])
def chat():
    msg = request.form["msg"]
    return GetChatResponse(msg)

def GetChatResponse(question):
    #Return answear from model
    return str(random.randint(0,100000))

if __name__=='__main__':
    app.run(debug=True)