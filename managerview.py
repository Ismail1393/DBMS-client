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
    if action == 'View Reservations':
        view_reservations()
    elif action == 'Edit Menu':
        edit_menu()
    elif action == 'Total Earnings':
        total_earnings()
    elif action == 'Manage Inventory':
        manage_inventory()


def view_reservations():
    """View current reservations."""
    print("Viewing Reservations...")
    conn = create_connection()
    try:
        query = "SELECT reservation_id, customer_name, reservation_time FROM Reservations WHERE reservation_time >= NOW()"
        cursor = conn.cursor()
        cursor.execute(query)
        print("Reservations:")
        for (reservation_id, customer_name, reservation_time) in cursor:
            print(f"ID: {reservation_id}, Customer: {customer_name}, Time: {reservation_time}")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()


def edit_menu():
    """Edit items in the menu."""
    print("Editing Menu...")
    conn = create_connection()
    try:
        item_name = input("Enter new menu item name: ")
        item_price = float(input("Enter price for the new item: "))
        query = "INSERT INTO MenuItems (name, price) VALUES (%s, %s)"
        cursor = conn.cursor()
        cursor.execute(query, (item_name, item_price))
        conn.commit()
        print("New menu item added.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()

def total_earnings():
    """Display total earnings."""
    print("Total Earnings...")
    conn = create_connection()
    try:
        query = "SELECT SUM(amount) AS TotalEarnings FROM Payments WHERE payment_date >= CURDATE()"
        cursor = conn.cursor()
        cursor.execute(query)
        total = cursor.fetchone()
        print("Total earnings today: $", total[0] if total[0] else 0)
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()


def manage_inventory():
    """Manage inventory items."""
    print("Managing Inventory...")
    conn = create_connection()
    try:
        query = "SELECT item_name, quantity FROM Inventory"
        cursor = conn.cursor()
        cursor.execute(query)
        print("Current Inventory:")
        for (item_name, quantity) in cursor:
            print(f"Item: {item_name}, Quantity: {quantity}")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()

