# main.py
from login_file import login
from menu import display_menu, manage_menu

def main():
    if login():
        while True:
            display_menu()
            choice = input()

            if choice == '1':
                print("Viewing Reservations...")
                # Placeholder for actual functionality
            elif choice == '2':
                manage_menu()
            elif choice == '3':
                print("Processing Payments...")
                # Placeholder for actual functionality
            else:
                print("Invalid option. Please try again.")
                continue

            # Check if the user wants to exit
            exit_option = input("Do you want to exit? (yes/no): ").lower()
            if exit_option == 'yes':
                print("Exiting...")
                break

if __name__ == "__main__":
    main()
