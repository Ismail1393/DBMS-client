import mysql.connector
from mysql.connector import Error

database_name = 'dmbs-project'
user = 'root'
password = 'ismail'

try:
    conn = mysql.connector.connect(host='localhost', password=password, user=user, database=database_name)
    if conn.is_connected():
        print("Connection established to", database_name)
    else:
        print("Connection failed to", database_name)
except Error as e:
    print(f"Error: {e}")
finally:
    if conn is not None and conn.is_connected():
        conn.close()