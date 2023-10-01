from components.config import Config
import pandas as pd

accounts_controls = pd.read_csv('components/accounts_controls.csv')

def TurnOnOff(feature, feature_name):
    if feature:
        print(f"{feature_name} is on. \nPress 1 to turn it off. \nPress 2 to exit.")
    else:
        print(f"{feature_name} is off. \nPress 1 to turn it on. \nPress 2 to exit.")
    choice = int(input("Your choice: "))
    if choice == 1:
        return True 
    else:
        return False

def guest_controls_selection():
    system_account_index = accounts_controls[(accounts_controls['first'] == Config.SYSTEM_ACCOUNT[0]) & (accounts_controls['last'] == Config.SYSTEM_ACCOUNT[1])].index[0]
    system_account = accounts_controls[(accounts_controls['first'] == Config.SYSTEM_ACCOUNT[0]) & (accounts_controls['last'] == Config.SYSTEM_ACCOUNT[1])]

    sms = system_account['sms'].values[0]
    email = system_account['email'].values[0]
    advertising = system_account['advertising'].values[0]

    while True:
        print("1. InCollege email")
        print("2. SMS")
        print("3. Targeted Advertising features")
        print("4. Exit")
        choice = int(input("Select an option to turn on/off one of the above: "))
        if choice == 1:
            if TurnOnOff(email, feature_name = "InCollege email"):
                accounts_controls.at[system_account_index, 'email'] = not email
                accounts_controls.to_csv('components/accounts_controls.csv', index=False)
            
        elif choice == 2:
            if TurnOnOff(sms, feature_name = "SMS"):
                accounts_controls.at[system_account_index, 'sms'] = not sms
                accounts_controls.to_csv('components/accounts_controls.csv', index=False)

        elif choice == 3:
            if TurnOnOff(advertising, feature_name = "Targeted Advertising features"):
                accounts_controls.at[system_account_index, 'advertising'] = not advertising
                accounts_controls.to_csv('components/accounts_controls.csv', index=False)

        elif choice == 4:
            break
        else:
            print("Invalid choice! Please select again.")
    

#function to handle language option
def language_option():
    system_account_index = accounts_controls[(accounts_controls['first'] == Config.SYSTEM_ACCOUNT[0]) & (accounts_controls['last'] == Config.SYSTEM_ACCOUNT[1])].index[0]
    system_account = accounts_controls[(accounts_controls['first'] == Config.SYSTEM_ACCOUNT[0]) & (accounts_controls['last'] == Config.SYSTEM_ACCOUNT[1])]

    language = system_account['language'].values[0]
    
    while True:
        print("1. English")
        print("2. Spanish")
        print("3. Exit")
        print(f"Your current language is {language}")
        choice = int(input("Select an option to change the language: "))
        if choice == 1:
            print("\nLanguage was set to English")
            accounts_controls.at[system_account_index, 'language'] = "English"
            accounts_controls.to_csv('components/accounts_controls.csv', index=False)
            break
        elif choice == 2:
            print("\nLanguage was set to Spanish")

            accounts_controls.at[system_account_index, 'language'] = "Spanish"
            accounts_controls.to_csv('components/accounts_controls.csv', index=False)
            break
        elif choice == 3:
            break
        
        else:
            print("\nInvalid choice! Please select again.")