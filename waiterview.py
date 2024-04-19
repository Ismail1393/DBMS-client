import os
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from processing_payments import process

def display_waiter_dashboard():
    """Display the waiter's dashboard with menu options."""
    print("--------------------------------------------------------------")
    print('                        \033[4mWaiters DashBoard\033[0m')
    print("--------------------------------------------------------------")

    action = inquirer.select(
        message="Select an action:",
        choices=[
            "Process Payments",
            "View Menu",
            "View Availability",
            "Place Order",
            Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()
    os.system('cls')

    # Handler for each action
    if action == 'Process Payments':
        process_payments()
    elif action == 'View Menu':
        view_menu()
    elif action == 'View Availability':
        view_availability()
    elif action == 'Place Order':
        place_order()

def process_payments():
    """Process payment transactions."""
    print("Processing Payments...")
    process()

def view_menu():
    """View the current menu items."""
    print("Viewing Menu...")
    # Placeholder for functionality

def view_availability():
    """Check table or resource availability."""
    print("Viewing Availability...")
    # Placeholder for functionality

def place_order():
    """Place a new order."""
    print("Placing Order...")
    # Placeholder for functionality
