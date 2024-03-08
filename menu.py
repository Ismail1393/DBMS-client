from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from processing_payments import process
import os
# Function to display manager menu
def display_menu():
    print("--------------------------------------------------------------")
    print('                        \033[4mManagers DashBoard\033[0m')
    print("--------------------------------------------------------------")

    action = inquirer.select(
        message="Select an action:",
        choices=[
            "View Reservations",
            "Edit Menu",
            "Process Payments",
            Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()
    os.system('cls')

    if action == 'Process Payments':
        process()
# Function to handle the "Manage Menu" option
def manage_menu():
    print("--------------------------------------------------------------")
    print('                        \033[4mEdit Menu\033[0m')
    print("--------------------------------------------------------------")
