from components.config import Config
import components.login as login
import components.menu_helper as menu_helper
import components.search as search
import components.friends as friends
import pandas as pd

accounts = pd.read_csv('components/accounts.csv')
accounts_controls = pd.read_csv('components/accounts_controls.csv')

# --------------------------Display Functions--------------------------
"""Function to display 2 groups of links"""
def display_groups_of_links():
    print("\n1. Useful Links")
    print("2. InCollege Important Links")
    print("3. Search for Jobs")
    print("4. Find people you know")
    print("5. Sign up/Log in")
    print("6. Exit menu")

"""Function to display useful links"""
def display_useful_links():
    print("\nUseful Links:")
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Go Back to Previous Menu")

"""Function to display important links"""
def display_inCollege_important_link():
    print("\nInCollege Important Links:")
    print("1. A Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Privacy Policy")
    print("6. Cookie Policy")
    print("7. Brand Policy")
    print("8. Copyright Policy")
    print("9. Languages")
    print("10. Go Back to Previous Menu")

"""Function to display general links in useful links"""
def display_general_links(isLogin = False):
    print("\nGeneral Links:")
    if not isLogin:
        print("1. Sign Up")
    else:
        print("1. Sign Out")
        Config.FLAG = False
        Config.SYSTEM_ACCOUNT = None
    print("2. Help Center")
    print("3. About")
    print("4. Press")
    print("5. Blog")
    print("6. Careers")
    print("7. Developers")
    print("8. Go Back to Previous Menu")


# --------------------------Selection Functions--------------------------
"""Selection function for useful links"""
def useful_links_user_selection():
    while True:
        display_useful_links()

        choice = int(input("Select an option: "))
        if choice == 1:
            while True:
                display_general_links(Config.FLAG)
                general_choice = int(input("Select an option: "))
                if general_choice == 8:
                    break
                general_link_selection(general_choice, Config.FLAG)

        elif choice == 2 or choice == 3 or choice == 4:
            print("\nUnder construction")
            break

        elif choice == 5:
            break

        else:
            print("\nInvalid choice. Please try again.") 

"""Selection function for important links"""
def incollege_important_links_user_selection():
    while True:
        display_inCollege_important_link()
        choice = int(input("Select an option: "))
        if choice == 1:
            print("Copy right\n@ 2023 James Anderson LLC")
        elif choice == 2:
            print("InCollege is an online tool that will be designed exclusively for college students. The platform allows student at different universities to connect, exchange information, and talk with each other. Students will use this tool while they are in college and then transition to LinkedIn once they get a job and leave school")
        elif choice == 3:
            print("Accessiblity, Acquire knowledge of and abide by WCAG 2.1, the Web Content Accessibility Guidelines.")
        elif choice == 4:
            print("By using this website, you agree that your data will be collected for recruiting purposes")
        elif choice == 5:
            print("Privacy Policy\nThis privacy notice for James Anderson LLC describes how and why we might collect, store, use, and/or share your information when you use our services")
            if not Config.FLAG:
                print("\nPlease log in to your account before setting")
                login.login()
                break
            print("Select 1 for Guest Controls, anything else to exit")
            c = int(input("Your choice: "))
            if c == 1:
                menu_helper.guest_controls_selection()
        elif choice == 6:
            print("We use cookies for various purposes, including but not limited to:\n\tEssential Cookies: These cookies are necessary for the proper functioning of our website. They enable you to navigate our site and use its features, such as accessing secure areas and making transactions.\n\tPerformance Cookies: These cookies help us analyze how visitors use our website. They allow us to improve the performance and functionality of our site by collecting and reporting information on things like page load times and error messages.\n\tFunctional Cookies: Functional cookies allow us to remember your preferences and settings, such as language preferences and customization options, to enhance your experience on our website.\n\tAdvertising Cookies: We and our advertising partners may use cookies to deliver advertisements that are relevant to your interests. These cookies may collect information about your browsing habits and serve you with tailored advertising content.\n\tAnalytics Cookies: We may use analytics cookies to gather information about how our website is used and to help us improve it. These cookies collect information in an anonymous form, such as the number of visitors to our site and which pages are most ")
        elif choice == 7:
            print("This Brand Policy outlines the guidelines and standards for the use and representation of the inCollege brand and associated assets. The purpose of this policy is to ensure consistency, integrity, and the protection of our brand identity across all communication channels and materials.")
        elif choice == 8:
            print("4. Restrictions on Use\n\tReproduction and Distribution: Unauthorized reproduction, distribution, or public display of copyrighted materials from our website or platforms is prohibited without our explicit permission or unless permitted by law.\n\tModification and Derivative Works: Users are not allowed to modify, create derivative works from, or alter our copyrighted materials without prior written consent.\n\tRemoval of Copyright Notices: Removing or altering copyright notices, watermarks, or any form of attribution on copyrighted materials is strictly prohibited.")
        elif choice == 9:
            if not Config.FLAG:
                print("\nPlease log in to your account before setting languages")
                login.login()
            menu_helper.language_option()
        elif choice == 10:
            break
        else:
            print("\nInvalid choice. Please try again.")

"""Selection function for general links in useful links"""
def general_link_selection(choice, isLogin = False):
    if choice == 1 and not isLogin:
        print("Redirecting to Sign Up / Login page")
        print()
        login.login()
    elif choice == 1 and isLogin:
        print("Redirecting to Sign Up page")
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


# --------------------------Main Function--------------------------
def general_menu():
    while True:
        display_groups_of_links()
        choice = int(input("Select an option: "))
        if choice == 1:
            # When user choose useful links
            useful_links_user_selection()
            
        elif choice == 2:
            # When user choose inCollege important links
            incollege_important_links_user_selection()  
        
        elif choice == 3:
            # When user choose inCollege for searching jobs
            search.search() 
        
        elif choice == 4:
            # When user choose inCollege for friends
            friends.friends()

        elif choice == 5:
            # Option for login in
            login.login()
        elif choice == 6:
            # Exit menu
            break
        else:
            print("Invalid choice. Please try again.")
        



