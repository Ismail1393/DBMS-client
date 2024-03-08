from InquirerPy import inquirer
from InquirerPy.base.control import Choice
# Function to display manager menu
def display_menu():
    print("--------------------------------------------------------------")
    print('                        \033[4mManagers DashBoard\033[0m')
    print("--------------------------------------------------------------")
    # print("1. View Reservations")
    # print("2. Manage Menu")
    # print("3. Process Payemnts")
    # print("Please enter the number of the menu option you would like to access:")
    action = inquirer.select(
        message="Select an action:",
        choices=[
            "View Reservations",
            "Manage Menu",
            "Process Payments",
            Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()
# Function to handle the "Manage Menu" option
def manage_menu():
    print("\n--- Manage Menu ---")
