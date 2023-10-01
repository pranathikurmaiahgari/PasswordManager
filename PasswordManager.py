import json
import getpass

# Define a dictionary to store passwords
passwords = {}

# Function to add a new password
def add_password():
    website = input("Enter website or app name: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    passwords[website] = {"username": username, "password": password}
    save_passwords()

# Function to retrieve a password
def get_password():
    website = input("Enter website or app name: ")
    if website in passwords:
        print(f"Username: {passwords[website]['username']}")
        print(f"Password: {passwords[website]['password']}")
    else:
        print("Website not found in the password manager.")

# Function to save passwords to a JSON file
def save_passwords():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Function to load passwords from the JSON file
def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Main program loop
if __name__ == "__main__":
    passwords = load_passwords()
    
    while True:
        print("\nPassword Manager Menu:")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
