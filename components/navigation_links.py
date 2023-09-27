import pandas as pd
from components.config import Config
import components.login as login

#function to print the first set of useful links
def display_useful_links():
    print("\nUseful Links:")
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Go Back to Previous Menu")

#function to print the links within "General"
def display_general_links():
    print("\nGeneral Links:")
    print("1. Sign Up")
    print("2. Help Center")
    print("3. About")
    print("4. Press")
    print("5. Blog")
    print("6. Careers")
    print("7. Developers")
    print("8. Go Back to Previous Menu")

#helper function to help handle the links within "General"
def general_link_selection(choice):
    if choice == 1:
        print("Redirecting to Sign Up / Login page")
        print()
        #calling login() function
        login.login()
    elif choice == 2:
        print("\nWe're here to help")
    elif choice == 3:
        print("\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
    elif choice == 4:
        print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports")
    elif choice == 5:
        print("\nUnder construction")
    elif choice == 6:
        print("\nUnder construction")
    elif choice == 7:
        print("\nUnder construction")
    else:
        print("\nInvalid Choice. Please Try Again")

#main function to call both links
def general_menu():
    while True:
        display_useful_links()
        choice = int(input("Select an option: "))

        if choice == 1:
            while True:
                display_general_links()
                general_choice = int(input("Select an option: "))
                if general_choice == 8:
                    break
                general_link_selection(general_choice)

        elif choice == 2 or choice == 3 or choice == 4:
            print("\nUnder construction")

        elif choice == 5:
            break

        else:
            print("\nInvalid choice. Please try again.")



