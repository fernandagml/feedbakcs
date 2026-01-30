from flask import Flask as F, render_template as rt

app = F(__name__)

@app.route("/")
def index():
    return rt("index.html")

@app.route("/sobremim")
def sobremim():
    return rt("sobremim.html")

app.run(host="0.0.0.0", port=5050, debug=True)