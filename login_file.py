import os
from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator
# login.py

valid_username = "user123"
valid_password = "pass123"

def login():
    print("--------------------------------------------------------------")
    print('        \033[4mWelcome to the Restaurant Management Interface\033[0m')
    print("--------------------------------------------------------------")

    # Get username and password
    username = inquirer.secret(
        message="Enter Username:",
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
