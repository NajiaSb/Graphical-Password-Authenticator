import os
from os.path import join, dirname, realpath
import hashlib
import application.db.user_db as user_db
from application.db.user_db import DuplicateEmailError, register_user
from application.db.user_db import DuplicateUsernameError, register_user
import sqlite3 as db

from application import app
from flask import render_template, request, json, redirect, url_for
UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/images/')
SQLPATH = join(dirname(realpath(__file__)), "graphical_password.db")

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
    username = ""
    email = ""
    password_hash= ""
    birthday = ""
    error = None 
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("selected_images")
        birthday = request.form.get("birthday")

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

    input_dict = {'username': username, 'birthday': birthday, 'email': email, 'password': password_hash}
    try:
        register_user(input_dict)
        return "Signup successful"

    except DuplicateEmailError:
        error ="Email already exists in the database"
    except DuplicateUsernameError:
            error ="Username already exists in the database"
    
    return render_template("signup.html", imageData=imageData, error=error)


imageData = [{"image": "../static/images/image1.png", "alt": "image1.png"}, 
    {"image": "../static/images/image2.png", "alt": "image2.png"}, 
    {"image": "../static/images/image3.png", "alt": "image3.png"}, 
    {"image": "../static/images/image4.png", "alt": "image4.png"},
    {"image": "../static/images/image5.png", "alt": "image5.png"},
    {"image": "../static/images/image6.png", "alt": "image6.png"},
    {"image": "../static/images/image7.png", "alt": "image7.png"},
    {"image": "../static/images/image8.png", "alt": "image8.png"},
    {"image": "../static/images/image9.png", "alt": "image9.png"},
    {"image": "../static/images/image10.png", "alt": "image10.png"},
    {"image": "../static/images/image11.png", "alt": "image11.png"},
    {"image": "../static/images/image12.png", "alt": "image12.png"},
    {"image": "../static/images/image13.png", "alt": "image13.png"},
    {"image": "../static/images/image14.png", "alt": "image14.png"},
    {"image": "../static/images/image15.png", "alt": "image15.png"},
    {"image": "../static/images/image16.png", "alt": "image16.png"},
    {"image": "../static/images/image17.png", "alt": "image17.png"},
    {"image": "../static/images/image18.png", "alt": "image18.png"},
    {"image": "../static/images/image19.png", "alt": "image19.png"},
    {"image": "../static/images/image20.png", "alt": "image20.png"},
    {"image": "../static/images/image21.png", "alt": "image21.png"},
    {"image": "../static/images/image22.png", "alt": "image22.png"},
    {"image": "../static/images/image23.png", "alt": "image23.png"},
    {"image": "../static/images/image24.png", "alt": "image24.png"},
    {"image": "../static/images/image25.png", "alt": "image25.png"},
    {"image": "../static/images/image26.png", "alt": "image26.png"},
    {"image": "../static/images/image27.png", "alt": "image27.png"},
    {"image": "../static/images/image28.png", "alt": "image28.png"},
    {"image": "../static/images/image29.png", "alt": "image29.png"},
    {"image": "../static/images/image30.png", "alt": "image30.png"},
    {"image": "../static/images/image31.png", "alt": "image31.png"},
    {"image": "../static/images/image32.png", "alt": "image32.png"},
    {"image": "../static/images/image33.png", "alt": "image33.png"},
    {"image": "../static/images/image34.png", "alt": "image34.png"},
    {"image": "../static/images/image35.png", "alt": "image35.png"}]
