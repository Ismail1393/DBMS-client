from dbconnect import create_connection

def process():
    print("\033[4mProcessing Payments\033[0m")
    conn = create_connection()  
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM dbmsproject.customers;"
            cursor.execute(query)
            records = cursor.fetchall()
            for row in records:
                print(row)  # Print each customer record
            cursor.close()
        except Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")

