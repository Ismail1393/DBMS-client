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
    conn = create_connection()
    try:
        order_id = input("Enter order ID to process payment: ")
        query = "UPDATE Orders SET paid = TRUE WHERE order_id = %s"
        cursor = conn.cursor()
        cursor.execute(query, (order_id,))
        conn.commit()
        print("Payment processed for order:", order_id)
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()


def view_menu():
    """View the current menu items."""
    print("Viewing Menu...")
    conn = create_connection()
    try:
        query = "SELECT * FROM MenuItems"
        cursor = conn.cursor()
        cursor.execute(query)
        for (item_id, name, price) in cursor:
            print(f"ID: {item_id}, Name: {name}, Price: {price}")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()


def view_availability():
    """Check table or resource availability."""
    print("Viewing Availability...")
    conn = create_connection()
    try:
        query = "SELECT table_id, available FROM Tables WHERE available = TRUE"
        cursor = conn.cursor()
        cursor.execute(query)
        available_tables = cursor.fetchall()
        if available_tables:
            for (table_id, available) in available_tables:
                print(f"Table {table_id} is available.")
        else:
            print("No tables available at the moment.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()


def place_order():
    """Place a new order."""
    print("Placing Order...")
    conn = create_connection()
    try:
        customer_id = input("Enter customer ID: ")
        table_id = input("Enter table ID: ")
        menu_item_id = input("Enter menu item ID: ")
        query = "INSERT INTO Orders (customer_id, table_id, menu_item_id, paid) VALUES (%s, %s, %s, FALSE)"
        cursor = conn.cursor()
        cursor.execute(query, (customer_id, table_id, menu_item_id))
        conn.commit()
        print("Order placed successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()
