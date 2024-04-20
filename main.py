# main.py
import os
from login_file import loginmenu
from processing_payments import process
from dbconnect import create_connection
from managerview import display_manager_dashboard
from waiterview import display_waiter_dashboard
from mysql.connector import errors    

def main():
    os.system('cls')
    while 1:
        success, user = loginmenu()
        if success:
            while True:
                #creating database connection
                conn = create_connection()
                if conn is not None:
                    try:
                        cursor = conn.cursor()
                        query = "SELECT permission_level FROM users WHERE email = %s;"
                        cursor.execute(query, (user,))
                        permission = cursor.fetchone()
                        if permission[0] == 2:
                            display_manager_dashboard()
                        elif permission[0] == 1:
                            display_waiter_dashboard()
                        else:
                            print("Invalid Permission Level")
                            return False

                    except errors.ProgrammingError as e:
                        print(f"Error: {e}")
                    finally:
                        cursor.close()
                        conn.close()
                else:
                    print("Failed to connect to the database.")


if __name__ == "__main__":
    main()
