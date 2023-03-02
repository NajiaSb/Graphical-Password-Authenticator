from application import app
from flask import render_template, request

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False)

@app.route("/login", methods=["POST", "GET"])
def login():
    imageData = [{"image": "../static/images/image.png", "alt": "image1"}, 
                 {"image": "../static/images/image.png", "alt": "image2"}, 
                 {"image": "../static/images/image.png", "alt": "image3"}, 
                 {"image": "../static/images/image.png", "alt": "image4"}]
    
    if request.method == "POST":
        username = request.form["username"]
        selected_images = request.form.getlist("selected_images")
        return "Successful Login!!"
    return render_template("login.html", imageData=imageData)



@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        birthday = request.form.get("birthday")
        email = request.form.get("email")
        selected_images = request.form.get("selected_images")
        return "Congrats,You Succcesfully registered!!"
    
    imageData = [{"image": "../static/images/image.png", "alt": "image1"}, 
                 {"image": "../static/images/image.png", "alt": "image2"}, 
                 {"image": "../static/images/image.png", "alt": "image3"}, 
                 {"image": "../static/images/image.png", "alt": "image4"}]
    return render_template("signup.html", imageData=imageData)
