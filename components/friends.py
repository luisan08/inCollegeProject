from components import Config
from components.login import login

def friends():
    if not Config.FLAG:
            print("\nPlease log in to your account before finding friends and connections")
            login.login()
    print("\nOptions:\n1. Find someone you know\n2.Show my network\n3. Quit Search")
    choice = int(input("Please enter your choice: "))
    while True:
        if choice == 1:
            print("Under construction.")
            break
        elif choice == 2:
            print("Under construction.")
            break
        elif choice == 3:
            break
        else:
            choice = int(input("Invalid choice. Please enter a valid choice: "))
    return