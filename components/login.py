import pandas as pd
from components.config import Config


"""This module contains functions for logging in to an existing account or creating a new account."""

"""Store accounts in a csv file. Each row contains a username and password."""
accounts = pd.read_csv('components/accounts.csv')

def in_InCollege_System():
    """Function for checking if user is in the InCollege system."""
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    if (first, last) in zip(accounts['first'], accounts['last']):
        print("\nWelcome back, " + first + " " + last + "! You are part of the InCollege system.\n")
        return True
    else:
        print("\nYou are not yet a part of the InCollege system yet.\n")
        return False

def get_first_last_name(username, password):  
    account_row = accounts[(accounts['username'] == username) & (accounts['password'] == password)]
    if not account_row.empty:
        first_name = account_row['first'].values[0]
        last_name = account_row['last'].values[0]
        return first_name, last_name
    else:
        return None, None

def login_existing_account():
    """Function for logging into an existing account."""
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if (username, password) in zip(accounts['username'], accounts['password']):
            print("You have successfully logged in!")
            first_name, last_name =  get_first_last_name(username, password)
            Config.SYSTEM_ACCOUNT = (first_name, last_name)
            Config.FLAG = 1
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
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    newAccount = {'username': username, 'password': password, 'first': first, 'last': last}
    
    newAccount = pd.DataFrame(newAccount, index=[0])
    accounts = pd.concat([accounts, newAccount], ignore_index=True)
    accounts.to_csv('components/accounts.csv', index=False)
    print("You have successfully created an account!")

def login():
    """Login function."""

    print("1. Create a new account")
    print("2. Login to existing account")
    
    option = input("Please select an option by entering a number: ")
    while option != "1" and option != "2":
        print("Invalid option. Please try again.")
        print("1. Create a new account")
        print("2. Login to existing account")
        option = input("Please select an option by entering a number: ")
    if option == "1":
        create_new_account()
    elif option == "2":
        login_existing_account()

