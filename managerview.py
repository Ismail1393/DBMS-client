import os
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from processing_payments import process

def display_manager_dashboard():
    """Display the manager's dashboard with menu options."""
    print("--------------------------------------------------------------")
    print('                        \033[4mManagers DashBoard\033[0m')
    print("--------------------------------------------------------------")

    action = inquirer.select(
        message="Select an action:",
        choices=[
            "View Reservations",
            "Edit Menu",
            "Process Payments",
            "Total Earnings",
            "Manage Inventory",
            Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()
    os.system('cls')

    # Handler for each action
    if action == 'Process Payments':
        process_payments()
    elif action == 'View Reservations':
        view_reservations()
    elif action == 'Edit Menu':
        edit_menu()
    elif action == 'Total Earnings':
        total_earnings()
    elif action == 'Manage Inventory':
        manage_inventory()

def process_payments():
    """Process payment transactions."""
    print("Processing Payments...")
    process()

def view_reservations():
    """View current reservations."""
    print("Viewing Reservations...")
    # Placeholder for functionality

def edit_menu():
    """Edit items in the menu."""
    print("Editing Menu...")
    # Placeholder for functionality

def total_earnings():
    """Display total earnings."""
    print("Total Earnings...")
    # Placeholder for functionality

def manage_inventory():
    """Manage inventory items."""
    print("Managing Inventory...")
    # Placeholder for functionality
