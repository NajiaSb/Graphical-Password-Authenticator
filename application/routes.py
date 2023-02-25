from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    imageData = [{"image": "../static/images/image.png", "alt": "image1"}, 
                 {"image": "../static/images/image.png", "alt": "image2"}, 
                 {"image": "../static/images/image.png", "alt": "image3"}, 
                 {"image": "../static/images/image.png", "alt": "image4"}]
    return render_template("signup.html", imageData=imageData)