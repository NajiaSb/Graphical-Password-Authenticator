import os
from os.path import join, dirname, realpath
import hashlib
import application.db.user_db as user_db
from application.db.user_db import DuplicateEmailError, register_user
from application.db.user_db import DuplicateUsernameError, register_user
import sqlite3 as db
import random

from application import app
from flask import render_template, request, json, redirect, url_for
UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/images/')
SQLPATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "db/graphical_password.db")


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        error = None
        message = None

        username = request.form["username"]
        selected_images_str = request.form.get("selected_images")
        selected_images = selected_images_str.split(',')

        conn = db.connect(SQLPATH)
        cursor = conn.execute(
            "SELECT * FROM USERS WHERE USERNAME=?", (username,))
        row = cursor.fetchone()
        conn.close()

        # check if username exists in database
        if row is not None:
            # create password hasg
            password_hash = hashlib.sha512()
            for path in selected_images:
                with open((UPLOADS_PATH + path.strip()).replace(" ", ""), 'rb') as f:
                    data = f.read()
                    password_hash.update(data)
            # grab birthday as salt for password hash
            password_hash.update(row[3].encode())
            password_hash = password_hash.hexdigest()  # generate hash

            # generate results
            if row[0] == username and row[2] == password_hash:
                message = "Your account exists!"
            elif row[0] == username and row[2] != password_hash:
                error = "Wrong password, please try again!"
        else:
            error = "No account exists with the username!"
        return render_template("login.html", imageData=imageData, login=False, message=message, error=error)
    random.shuffle(imageData)

    return render_template("login.html", imageData=imageData, login=False, message=None, error=None)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    username = ""
    email = ""
    password_hash = ""
    birthday = ""
    error = None
    message = None

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("selected_images")
        birthday = request.form.get("birthday")

        image_paths = password.split(',')
        password_hash = hashlib.sha512()
        for path in image_paths:
            with open((UPLOADS_PATH + path).replace(" ", ""), 'rb') as f:
                data = f.read()
                password_hash.update(data)
        password_hash.update(birthday.encode())
        password_hash = password_hash.hexdigest()

        input_dict = {'username': username, 'birthday': birthday,
                      'email': email, 'password': password_hash}
        try:
            register_user(input_dict)
            message = "Signup successful"
            return render_template("signup.html", imageData=imageData, message=message)
        except DuplicateEmailError:
            error = "Email already exists in the database"
            return render_template("signup.html", imageData=imageData, error=error)
        except DuplicateUsernameError:
            error = "Username already exists in the database"
            return render_template("signup.html", imageData=imageData, error=error)

    return render_template("signup.html", imageData=imageData, message=None, error=None)


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
             {"image": "../static/images/image35.png", "alt": "image35.png"},
             {"image": "../static/images/image36.png", "alt": "image36.png"},
             {"image": "../static/images/image37.png", "alt": "image37.png"},
             {"image": "../static/images/image38.png", "alt": "image38.png"},
             {"image": "../static/images/image39.png", "alt": "image39.png"},
             {"image": "../static/images/image40.png", "alt": "image40.png"},
             {"image": "../static/images/image41.png", "alt": "image40.png"},
             {"image": "../static/images/image42.png", "alt": "image40.png"},
             {"image": "../static/images/image43.png", "alt": "image40.png"},
             {"image": "../static/images/image44.png", "alt": "image44.png"},
             {"image": "../static/images/image45.png", "alt": "image45.png"},
             {"image": "../static/images/image46.png", "alt": "image46.png"},
             {"image": "../static/images/image47.png", "alt": "image47.png"},
             {"image": "../static/images/image48.png", "alt": "image48.png"},
             {"image": "../static/images/image49.png", "alt": "image49.png"},
             {"image": "../static/images/image50.png", "alt": "image50.png"},
             {"image": "../static/images/image51.png", "alt": "image51.png"},
             {"image": "../static/images/image52.png", "alt": "image52.png"},
             {"image": "../static/images/image53.png", "alt": "image53.png"},
             {"image": "../static/images/image54.png", "alt": "image54.png"},
             {"image": "../static/images/image55.png", "alt": "image55.png"},
             {"image": "../static/images/image56.png", "alt": "image56.png"},]
