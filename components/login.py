import pandas as pd
"""This module contains functions for logging in to an existing account or creating a new account."""

"""Store accounts in a csv file. Each row contains a username and password."""
accounts = pd.read_csv('components/accounts.csv')

def login_existing_account():
    """Function for logging into an existing account."""
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        # for u, p in zip(accounts['username'], accounts['password']):
        #     if username == u and password == p:
        #         print("You have successfully logged in!")
        #         return False
        #     else:
        #         print("Incorrect username or password. Please try again!")
        if (username, password) in zip(accounts['username'], accounts['password']):
            print("You have successfully logged in!")
            return False
        else:
            print("Incorrect username or password. Please try again!")

def validate_password(password):
    """Helper function for validating password."""
    """Function returns True if password is valid, False otherwise."""
    if len(password) < 8 or len(password) > 12:
        print("Password must be between 8 and 12 characters long.")
        return False
    if not any(c.isupper() for c in password):
        print("Password must contain at least one capital letter.")
        return False
    if not any(c.isdigit() for c in password):
        print("Password must contain at least one digit.")
        return False
    if not any(not c.isalnum() for c in password):
        print("Password must contain at least one special character.")
        return False
    return True

def exceeded_login_attempts(attempts = 5):
    """Helper function for checking if login attempts have been exceeded."""
    """Function returns True if login attempts have been exceeded, False otherwise."""
    return len(accounts) >= attempts

def create_new_account():
    """Function for creating a new account."""
    global accounts 
    print(len(accounts))
    if exceeded_login_attempts():
        print("All permitted accounts have been created, please come back later.")
        return
    
    username = input("Please enter your username: ")
    while username in accounts['username']:
        username = input("Username already exists. Please enter a different username: ")
    print("Username is accepted.")
    print("Your password must be at least 8 characters and maximum 12 characters long.")
    print("Your password must contain at least one capital letter, one digit, and one special character.")
    password = input("Please enter your password: ")
    while not validate_password(password):
        password = input("Please enter your password: ")

    newAccount = {'username': username, 'password': password}
    
    newAccount = pd.DataFrame(newAccount, index=[0])
    accounts = pd.concat([accounts, newAccount], ignore_index=True)
    accounts.to_csv('components/accounts.csv', index=False)
    print("You have successfully created an account!")

def login():
    """Main login function."""
    print("1. Create a new account")
    print("2. Login to existing account")
    option = input("Please select an option by entering a number: ")
    if option == "1":
        create_new_account()
    elif option == "2":
        login_existing_account()
    else:
        print("Invalid option. Please try again.")
        login()

