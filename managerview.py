import os
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from processing_payments import process
from dbconnect import create_connection

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
            "View Employees",
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
    elif action == 'View Employees':
        employees()
    elif action == 'Edit Menu':
        edit_menu()
    elif action == 'Total Earnings':
        total_earnings()
    elif action == 'Manage Inventory':
        manage_inventory()



def view_reservations():
    print("--------------------------------------------------------------")
    print('                        \033[4mVeiwing Reservations\033[0m')
    print("--------------------------------------------------------------")
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
    print("--------------------------------------------------------------")
    print('                        \033[4mCurrent Menu Items\033[0m')
    print("--------------------------------------------------------------")
    conn = create_connection()
    if conn is None:
        print("Failed to connect to database.")
        return

    try:
        cursor = conn.cursor()

        # Display all current menu items
        cursor.execute("SELECT item_id, name, price, available FROM MenuItems")
        items = cursor.fetchall()
        print('\n')
        for item in items:
            item_id, name, price, available = item
            availability_status = 'Yes' if available == 1 else 'No'
            print(f"ID: {item_id}, Name: {name}, Price: ${price:.2f}, Available: {availability_status}")
        print('\n')

        operation = inquirer.select(
            message="Select an operation:",
            choices=[
                "Add New Menu Item",
                "Update Existing Menu Item", 
                "Toggle Availability of a Menu Item",
            ],
            default=None,
        ).execute()

        if operation == 'Add New Menu Item':
            item_name = input("Enter new menu item name: ")
            item_price = float(input("Enter price for the new item: "))
            query = "INSERT INTO MenuItems (name, price, available) VALUES (%s, %s, 1)"
            cursor.execute(query, (item_name, item_price))
            print("New menu item added.")
            os.system('cls')

        elif operation == 'Update Existing Menu Item':
            item_id = input("Enter the ID of the menu item to update: ")
            item_name = input("Enter new name for the menu item (leave blank to not change): ")
            item_price = input("Enter new price for the menu item (leave blank to not change): ")

            updates = []
            params = []

            if item_name:
                updates.append("name = %s")
                params.append(item_name)
            if item_price:
                updates.append("price = %s")
                params.append(float(item_price))

            if updates:
                query = f"UPDATE MenuItems SET {', '.join(updates)} WHERE item_id = %s"
                params.append(item_id)
                cursor.execute(query, params)
                print("Menu item updated.")
            else:
                print("No changes made.")
            os.system('cls')

        elif operation == 'Toggle Availability of a Menu Item':
            item_id = input("Enter the ID of the menu item to toggle availability: ")
            query = "UPDATE MenuItems SET available = CASE WHEN available = 1 THEN 0 ELSE 1 END WHERE item_id = %s"
            cursor.execute(query, (item_id,))
            print("Menu item availability toggled.")
            os.system('cls')

        else:
            print("Invalid choice.")
            os.system('cls')

        conn.commit()

    except mysql.connector.Error as err:
        print("Error:", err)
    except ValueError:
        print("Invalid input for price. Please enter a valid number.")
    finally:
        cursor.close()
        conn.close()

    

def total_earnings():
    """Display total earnings and calculate net profit for the day."""
    print("Total Earnings and Net Profit Calculation...")
    conn = create_connection()
    if not conn:
        print("Failed to connect to the database.")
        return

    try:
        cursor = conn.cursor()

        # Calculate total sales for the day
        sales_query = "SELECT SUM(amount) FROM Payments WHERE payment_date = CURDATE()"
        cursor.execute(sales_query)
        total_sales_result = cursor.fetchone()
        total_sales = total_sales_result[0] if total_sales_result else 0.0

        # Calculate total cost of dishes sold for the day
        cost_query = """
        SELECT SUM(mi.cost * oi.quantity) FROM OrderItems oi
        JOIN MenuItems mi ON oi.item_id = mi.item_id
        JOIN Orders o ON oi.order_id = o.order_id
        WHERE o.order_date = CURDATE()
        """
        cursor.execute(cost_query)
        total_cost_result = cursor.fetchone()
        total_cost = total_cost_result[0] if total_cost_result else 0.0

        # Calculate salaries paid for the day
        salaries_query = "SELECT SUM(daily_wage) FROM Employees"
        cursor.execute(salaries_query)
        total_salaries_result = cursor.fetchone()
        total_salaries = total_salaries_result[0] if total_salaries_result else 0.0

        # Calculate net profit
        net_profit = total_sales - (total_cost + total_salaries)

        # Print the calculated values
        print(f"Total sales today: ${total_sales:.2f}")
        print(f"Total cost of dishes sold today: ${total_cost:.2f}")
        print(f"Total salaries paid today: ${total_salaries:.2f}")
        print(f"Net profit today: ${net_profit:.2f}")

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if cursor:
            cursor.close()
        if conn:
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

def employees():
    """Fetch and display all employee information."""
    print("Fetching employee details...")
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        query = "SELECT employee_id, name, position, salary FROM Employees ORDER BY employee_id"
        cursor = conn.cursor()
        cursor.execute(query)
        print("Employee Details:")
        for employee in cursor:
            employee_id, name, position, salary = employee
            print(f"ID: {employee_id}, Name: {name}, Position: {position}, Salary: ${salary:.2f}")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()

  
