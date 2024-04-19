# main.py
from login_file import loginmenu
import os
from menu import display_menu, manage_menu
from processing_payments import process
from dbconnect import create_connection

def main():
    os.system('cls')
    if loginmenu():
        while True:
            display_menu()
            

if __name__ == "__main__":
    main()
