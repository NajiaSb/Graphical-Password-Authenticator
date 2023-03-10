import sqlite3 as db 
import os


UPLOADS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/images/')
SQLPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "graphical_password.db")

class DuplicateEmailError(Exception):
    pass

class DuplicateUsernameError(Exception):
    pass


def register_user(input_dict):

    conn = db.connect(SQLPATH)

    # Checks if the email exists in the database
    cursor = conn.execute("SELECT EMAIL FROM USERS WHERE EMAIL=?", (input_dict['email'],))
    row = cursor.fetchone()
    if row is not None:
        raise DuplicateEmailError('Email already exists in the database')

    # Checks if the username exists in the database
    cursor = conn.execute("SELECT USERNAME FROM USERS WHERE USERNAME=?", (input_dict['username'],))
    row = cursor.fetchone()
    if row is not None:
        raise DuplicateUsernameError('Username already exists in the database')

    conn.execute("INSERT INTO USERS (USERNAME, BIRTHDAY, EMAIL, PASSWORD_HASH) VALUES (?, ?, ?, ?)",
                 (input_dict['username'], input_dict['birthday'], input_dict['email'], input_dict['password']))
    conn.commit()
    conn.close()
