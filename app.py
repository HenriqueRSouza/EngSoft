from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mackenzie, meu nome e Henrique Ribeiro com o RA 10401770"
