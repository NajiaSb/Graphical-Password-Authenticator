from os.path import join, dirname, realpath
import hashlib
from application import app
from flask import render_template, request, json, redirect, url_for

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False)

@app.route("/login", methods=["POST", "GET"])
def login():
  
    
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
        password = request.form.get("selected_images")
        print("PASSWORD" + password + "\n")

        UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/images/')
   
        #  Hash the password using SHA-256
        image_paths = password.split(',')
        password_hash = hashlib.sha512()
        for path in image_paths:
            with open((UPLOADS_PATH + path).replace(" ", ""), 'rb') as f:
                data = f.read()
                password_hash.update(data)
        password_hash.update(birthday.encode())
        password_hash = password_hash.hexdigest()
        return redirect(url_for('index'))
    return render_template("signup.html", imageData=imageData)


imageData = [{"image": "../static/images/image1.png", "alt": "image1"}, 
    {"image": "../static/images/image2.png", "alt": "image2"}, 
    {"image": "../static/images/image3.png", "alt": "image3"}, 
    {"image": "../static/images/image4.png", "alt": "image4"},
    {"image": "../static/images/image5.png", "alt": "image5"},
    {"image": "../static/images/image6.png", "alt": "image6"},
    {"image": "../static/images/image7.png", "alt": "image7"},
    {"image": "../static/images/image8.png", "alt": "image8"},
    {"image": "../static/images/image9.png", "alt": "image9"},
    {"image": "../static/images/image10.png", "alt": "image10"},
    {"image": "../static/images/image11.png", "alt": "image11"},
    {"image": "../static/images/image12.png", "alt": "image12"},
    {"image": "../static/images/image13.png", "alt": "image13"},
    {"image": "../static/images/image14.png", "alt": "image14"},
    {"image": "../static/images/image15.png", "alt": "image15"},
    {"image": "../static/images/image16.png", "alt": "image16"},
    {"image": "../static/images/image17.png", "alt": "image17"},
    {"image": "../static/images/image18.png", "alt": "image18"},
    {"image": "../static/images/image19.png", "alt": "image19"},
    {"image": "../static/images/image20.png", "alt": "image20"},
    {"image": "../static/images/image21.png", "alt": "image21"},
    {"image": "../static/images/image22.png", "alt": "image22"},
    {"image": "../static/images/image23.png", "alt": "image23"},
    {"image": "../static/images/image24.png", "alt": "image24"},
    {"image": "../static/images/image25.png", "alt": "image25"},
    {"image": "../static/images/image26.png", "alt": "image26"},
    {"image": "../static/images/image27.png", "alt": "image27"},
    {"image": "../static/images/image28.png", "alt": "image28"},
    {"image": "../static/images/image29.png", "alt": "image29"},
    {"image": "../static/images/image30.png", "alt": "image30"},
    {"image": "../static/images/image31.png", "alt": "image31"},
    {"image": "../static/images/image32.png", "alt": "image32"},
    {"image": "../static/images/image33.png", "alt": "image33"},
    {"image": "../static/images/image34.png", "alt": "image34"},
    {"image": "../static/images/image35.png", "alt": "image35"}]