import pandas as pd
import json
from components.config import Config
import components.login as login

accounts = pd.read_csv('components/accounts.csv')
friendLists = json.load(open('components/friendLists.json'))

def send_request(username):
    for user in friendLists:
        if username in user:
            user[username]['pendingRequest'].append(Config.SYSTEM_ACCOUNT[2])
            break
    with open('components/friendLists.json', 'w') as f:
        json.dump(friendLists, f)
    return

def find_someone():
    last = input("Please enter the last name of the person you are looking for: ")
    university = input("Please enter the university of the person you are looking for: ")
    major = input("Please enter the major of the person you are looking for: ")
    print("Here are the results for your search: ")
    filtered_accounts = accounts[
        (accounts['last'] == last) & 
        (accounts['university'] == university) & 
        (accounts['major'] == major) &
        (accounts['username'] != Config.SYSTEM_ACCOUNT[2])
    ]
    if filtered_accounts.empty:
        print("No results found.")
    else:
        filtered_accounts = filtered_accounts.rename(columns={'first': 'First Name', 'last': 'Last Name', 'university': 'University', 'major': 'Major'})
        print(filtered_accounts[['First Name', 'Last Name', 'University', 'Major']].reset_index(drop=True))

        while True:
            choice = input("Choose the number of the person you want to connect or e to exit: ")
            if choice == 'e':
                return
            elif choice.isdigit():
                choice = int(choice)
                if choice >= 0 and choice < len(filtered_accounts):
                    username = filtered_accounts.iloc[choice]['username']
                    send_request(username)
                    first = filtered_accounts.iloc[choice]['First Name']
                    last = filtered_accounts.iloc[choice]['Last Name']
                    print("Sent request to " + first + " " + last + "!")
                else:
                    print(f"Choice must be between 0 and {len(filtered_accounts)}")
            else:
                choice = input("Invalid choice. Please enter a valid choice: ")

    return

def process_request(friend, system_account):
    for user in friendLists:
        if friend in user:
            user[friend]['friendList'].append(system_account)
        if system_account in user:
            user[system_account]['friendList'].append(friend)
    with open('components/friendLists.json', 'w') as f:
            json.dump(friendLists, f)

def notifications(username):
    for user in friendLists:
        if username in user:
            if not user[username]['pendingRequest']:
                return
            else:
                while True:
                    print("You have pending requests from: ")
                    requests = user[username]['pendingRequest']
                    if not requests:
                        return
                    matching_accounts = accounts[accounts['username'].isin(requests)][['first', 'last']].reset_index(drop=True)
                    print(matching_accounts)
                    
                    choice = input("Choose the request that you want to accept or deny or q to quit: ") 
                    if choice == 'q':
                        return
                    elif choice.isdigit():
                        choice = int(choice)

                        if choice >= 0 and choice < len(requests):
                            print("Do you want to add this person to your friend list?")
                            c = int(input("\n1. Accept\n2. Deny\nPlease enter your choice: "))
                            if c == 1:
                                process_request(requests[choice], Config.SYSTEM_ACCOUNT[2])

                            user[username]['pendingRequest'].remove(requests[choice])
                            with open('components/friendLists.json', 'w') as f:
                                json.dump(friendLists, f)
                        else:
                            print(f"Choice must be between 0 and {len(requests)}")        
    return

def accept_request(username):
    for user in friendLists:
        if username in user:
            if Config.SYSTEM_ACCOUNT[2] in user[username]['pendingRequest']:
                user[username]['pendingRequest'].remove(Config.SYSTEM_ACCOUNT[2])
                user[username]['friendList'].append(Config.SYSTEM_ACCOUNT[2])
                for system_user in friendLists:
                    if Config.SYSTEM_ACCOUNT[2] in system_user:
                        system_user[Config.SYSTEM_ACCOUNT[2]]['friendList'].append(username)
                        break
            else:
                print("No pending request from this user.")
            with open('components/friendLists.json', 'w') as f:
                json.dump(friendLists, f)
            return True
    return False

def reject_request(username):
    for user in friendLists:
        if username in user:
            if Config.SYSTEM_ACCOUNT[2] in user[username]['pendingRequest']:
                user[username]['pendingRequest'].remove(Config.SYSTEM_ACCOUNT[2])
                with open('components/friendLists.json', 'w') as f:
                    json.dump(friendLists, f)
                return True
            else:
                print("No pending request from this user.")
    return False

def show_my_network(username):
    for user in friendLists:
        if username in user:
            my_network = user[username]['friendList']
            if not my_network:
                print("You don't have any connections yet.")
            else:
                print("Your network:")
                for friend in my_network:
                    print(friend)
            return

def disconnect(username, friend_to_disconnect):
    for user in friendLists:
        if username in user:
            if friend_to_disconnect in user[username]['friendList']:
                user[username]['friendList'].remove(friend_to_disconnect)
                for friend in friendLists:
                    if friend_to_disconnect in friend:
                        friend[friend_to_disconnect]['friendList'].remove(username)
                        break
                with open('components/friendLists.json', 'w') as f:
                    json.dump(friendLists, f)
                return True
            else:
                print("You are not connected with this user.")
    return False

def friends():
    if not Config.FLAG:
        print("\nPlease log in to your account before finding friends and connections")
        login.login()
        return
    
    notifications(Config.SYSTEM_ACCOUNT[2])

    print("\nOptions:\n1. Find someone you know\n2. Show my network\n3. Quit Search")
    choice = int(input("Please enter your choice: "))
    while True:    
        if choice == 1:
            find_someone()
        elif choice == 2:
            show_my_network(Config.SYSTEM_ACCOUNT[2])
            while True:
                action = input("Enter 'd' to disconnect from a friend or 'q' to quit: ")
                if action == 'd':
                    friend_to_disconnect = input("Enter the username of the friend you want to disconnect from: ")
                    if disconnect(Config.SYSTEM_ACCOUNT[2], friend_to_disconnect):
                        print(f"You have disconnected from {friend_to_disconnect}.")
                    else:
                        print(f"You are not connected with {friend_to_disconnect}.")
                elif action == 'q':
                    break
                else:
                    print("Invalid choice. Please enter 'd' or 'q'.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

    return
