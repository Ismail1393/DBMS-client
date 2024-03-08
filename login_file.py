# login.py
def login():
    print("Welcome to the CLI Login Interface")

    # Get username and password
    username = input("Enter your username: ")
    password = input("Enter your password (getpass disabled for this environment): ")  # Modified line

    # Simulate authentication (replace this with your actual authentication logic)
    if authenticate(username, password):
        print("Login successful. Welcome, {}!".format(username))
        # Call your main function or perform other tasks after successful login
        return True
    else:
        print("Login failed. Exiting program.")
        return False

def authenticate(username, password):
    # Replace this with your actual authentication logic
    valid_username = "user123"
    valid_password = "pass123"
    
    return username == valid_username and password == valid_password
