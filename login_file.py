import os
import bcrypt
from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator
from dbconnect import create_connection
from mysql.connector import errors

# login.py

valid_username = "user123"
valid_password = "pass123"

def loginmenu():
    print("--------------------------------------------------------------")
    print('        \033[4mWelcome to the Restaurant Management Interface\033[0m')
    print("--------------------------------------------------------------")
    action = inquirer.select(
        message="Select an action:",
        choices=[
            "Login",
            "Signup",
            "Exit",
        ],
        default=None,
    ).execute()
    os.system('cls')

    if action == "Login":
        login()
    elif action == "Signup":
        signup()
        

def login():
    # Get username and password
    username = inquirer.secret(
        message="Enter Username/Email:",
        validate=lambda text: text == valid_username,
        invalid_message="Wrong Username",
       long_instruction="Username is user123",
    ).execute()

    password = inquirer.secret(

        message="Enter password:",
        validate=lambda text: text == valid_password,
        invalid_message="Wrong password",
        long_instruction="Original password: pass123",
    ).execute()
    confirm = inquirer.confirm(message="Confirm?", default=True).execute()
    os.system('cls')
    return True

def signup():

    first_name = inquirer.text(
        message="Enter First Name:",
        validate=lambda text: len(text) > 0,
        invalid_message="First Name cannot be empty",
    ).execute()

    last_name = inquirer.text(
        message="Enter Last Name:",
        validate=lambda text: len(text) > 0,
        invalid_message="Last Name cannot be empty",
    ).execute()

    username = inquirer.text(
        message="Enter Username/Email:",
        validate=lambda text: len(text) > 0,
        invalid_message="Username cannot be empty",
    ).execute()

    password = inquirer.text(
        message="Enter password:",
        validate=lambda text: len(text) >= 8,
        invalid_message="Password must be at least 8 characters long",
    ).execute()

    confirm = inquirer.confirm(message="Confirm?", default=True).execute()
    
    # #hashing the password
    hashedpw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    #creating database connection
    conn = create_connection()  
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (first_name, last_name, permission_level, email, password) VALUES ( %s, %s, %s, %s, %s);"
            values = (first_name, last_name, 0, username, hashedpw)
            cursor.execute(query, values)
            conn.commit()
            print("User added successfully")
            cursor.close()
        except errors.ProgrammingError as e:
            print(f"Error: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")
    
    # os.system('cls')
    return True
    