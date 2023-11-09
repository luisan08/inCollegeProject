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
        json.dump(friendLists, f, indent=4)
    return

def send_message(username):
    for user in friendLists:
        if username in user:
            if Config.SYSTEM_ACCOUNT[2] in user[username]['friendList'] or Config.SYSTEM_ACCOUNT[3] == 'Plus':
                message = input("Enter your message: ")
                user[username]['inbox'].append({Config.SYSTEM_ACCOUNT[2]: message})
                print("Message sent!")
                with open('components/friendLists.json', 'w') as f:
                    json.dump(friendLists, f, indent=4)
                return
            else:
                print("You are not friends with this person")
                return

def find_someone():
    last = input("Please enter the last name of the person you are looking for: ")
    university = input("Please enter the university of the person you are looking for: ")
    major = input("Please enter the major of the person you are looking for: ")
    print("Here are the results for your search: ")
    filtered_accounts = pd.DataFrame(columns=['first', 'last', 'university', 'major', 'username'])
    i = 0
    for user in accounts.itertuples():
        if user.last == last or user.university == university or user.major == major:
            if user.username == Config.SYSTEM_ACCOUNT[2]:
                continue
            filtered_accounts.loc[i] = [user.first, user.last, user.university, user.major, user.username]
            i += 1

    if filtered_accounts.empty:
        print("No results found.")
    else:
        filtered_accounts = filtered_accounts.rename(columns={'first': 'First Name', 'last': 'Last Name', 'university': 'University', 'major': 'Major'})
        print(filtered_accounts[['First Name', 'Last Name', 'University', 'Major']].reset_index(drop=True))
        option = int(input("1. Send a connection request\n2. Send message\nPlease enter your choice: "))
        if option == 1:
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
        elif option == 2:
            choice = input("Choose the number of the person you want to send the message or e to exit: ")
            if choice == 'e':
                return
            elif choice.isdigit():
                choice = int(choice)
                if choice >= 0 and choice < len(filtered_accounts):
                    username = filtered_accounts.iloc[choice]['username']
                    first = filtered_accounts.iloc[choice]['First Name']
                    last = filtered_accounts.iloc[choice]['Last Name']
                    send_message(username)
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
            json.dump(friendLists, f, indent=4)

def notifications(username):
    for user in friendLists:
        if username in user:
            if not user[username]['pendingRequest'] and not user[username]['inbox']:
                return
            elif user[username]['pendingRequest']:
                while True:
                    requests = user[username]['pendingRequest']
                    if not requests:
                        return
                    print("You have pending requests from: ")
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
                                json.dump(friendLists, f, indent=4)
                        else:
                            print(f"Choice must be between 0 and {len(requests)}")        
            else:
                while True:
                    inbox = user[username]['inbox']
                    if not inbox:
                        return
                    print("You have messages from: ")
                    for i in inbox:
                        matching_accounts = accounts[accounts['username'].isin(list(i.keys()))][['first', 'last']].reset_index(drop=True)

                    print(matching_accounts)

                    choice = input("Choose the message that you want to read or q to quit: ")
                    if choice == 'q':
                        return
                    elif choice.isdigit():
                        choice = int(choice)
                        if choice >= 0 and choice < len(inbox):
                            print(f'Message from {matching_accounts.iloc[choice]["first"]} {matching_accounts.iloc[choice]["last"]}: ')
                            print(list(user[username]['inbox'][choice].values())[0])
                            c = int(input("Do you want to check the message?\n1. Reply\n2. Delete from inbox\nPlease enter your choice: "))
                            if c == 1:
                                send_message(list(user[username]['inbox'][choice].keys())[0])
                                user[username]['inbox'].remove(inbox[choice])
                            if c == 2:
                                user[username]['inbox'].remove(inbox[choice])
                                print("Message deleted!")
                                with open('components/friendLists.json', 'w') as f:
                                    json.dump(friendLists, f, indent=4)
                        else:
                            print(f"Choice must be between 0 and {len(inbox)}")          
    return

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

def show_all_people():
    print("All people on InCollege: ")
    all_people = accounts.loc[accounts['username'] != Config.SYSTEM_ACCOUNT[2]]
    all_people = all_people[['username', 'first', 'last', 'university', 'major']].reset_index(drop=True)
    print(all_people[['first', 'last', 'university', 'major']].reset_index(drop=True))

    return all_people

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
                    json.dump(friendLists, f, indent=4)
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

    #print("\nOptions:\n1. Find someone you know\n2. Show my network\n3. Quit Search")
    choice = None
    while True:  
        print("\nOptions:\n1. Find/Message someone you know\n2. Show my network\n3. Show all people\n4. Quit Search")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            find_someone()
        elif choice == 2:
            show_my_network(Config.SYSTEM_ACCOUNT[2])
            action = None
            while action != 'd' and action != 'q':
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
            if Config.SYSTEM_ACCOUNT[3] == 'Plus':
                all_people = show_all_people()
                action = input("Enter the number of the person you want to send message with or q to quit: ")
                if action == 'q':
                    break
                elif action.isdigit():
                    action = int(action)
                    if action >= 0 and action < len(all_people):
                        username = all_people.iloc[action]['username']
                        send_message(username)
                    else:
                        print(f"Choice must be between 0 and {len(all_people)}")
                else:
                    action = input("Invalid choice. Please enter a valid choice: ")
            else:
                print("You must be a Plus member to view all people.")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

    return
