import json
from components.config import Config
from components import login
import string

def create_profile(username):
    with open('components/profile.json', 'r') as f:
        profiles = json.load(f)

    if username not in profiles:
        profiles[username] = {}  # Create an empty profile if it doesn't exist

    user_profile = profiles[username]

    # Function to update a section of the profile
    def update_section(section_name, section_data):
        user_profile[section_name] = section_data
        print(f"{section_name.capitalize()} section updated successfully.")

    # Ask the user which section they want to update
    while True:
        print("\nProfile Sections:")
        print("1. Title")
        print("2. Major")
        print("3. University")
        print("4. About")
        print("5. Experiences")
        print("6. Education")
        print("7. Finish and Save")
        choice = int(input("Select a section to update or 7 to finish: "))

        if choice == 1:
            title = input('Enter a title for your profile: ')
            update_section('title', title)
        elif choice == 2:
            major = string.capwords(input('Enter your major: '))
            update_section('major', major)
        elif choice == 3:
            university = string.capwords(input('Enter the University you attend currently: '))
            update_section('university', university)
        elif choice == 4:
            about = input('Describe yourself: ')
            update_section('about', about)
        elif choice == 5:
            num_of_experience = int(input('How much previous work experience do you have? (Up to 3 previous jobs) '))
            while num_of_experience > 3 or num_of_experience < 0:
                num_of_experience = int(input('Number of previous jobs cannot be greater than 3. Please try again: '))
            experience = []
            for i in range(num_of_experience):
                new_experience = {}
                new_experience['title'] = input('Title of Experience: ')
                new_experience['employer'] = string.capwords(input('Employer: '))
                new_experience['date_start'] = input('Date Started: ')
                new_experience['date_end'] = input('Date Ended: ')
                new_experience['location'] = string.capwords(input('Location: '))
                new_experience['description'] = input('Description of work done: ')
                experience.append(new_experience)
            update_section('experience', experience)
        elif choice == 6:
            num_of_education = int(input('How many higher level institutions have you attended? '))
            while num_of_education < 1:
                num_of_education = int(input('Number must be 1 or greater. Please try again: '))
            education = []
            for i in range(num_of_education):
                new_education = {}
                new_education['school'] = string.capwords(input('School: '))
                new_education['degree'] = string.capwords(input('Degree: '))
                new_education['year_attended'] = input('Years Attended: ')
                education.append(new_education)
            update_section('education', education)
        elif choice == 7:
            # Save the updated profile to the JSON file
            with open('components/profile.json', 'w') as f:
                json.dump(profiles, f, indent=4)
            print("Profile saved successfully.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

def view_profile(username):
    with open('components/profile.json', 'r') as f:
        profiles = json.load(f)

    if username in profiles:
        user_profile = profiles[username]
   

        print(f"\n{username}'s Profile: ")
        print(f"Title: {user_profile.get('title', user_profile.get('dafault'))}")
        print(f"Major: {user_profile.get('major', user_profile.get('dafault'))}")
        print(f"University: {user_profile.get('university', user_profile.get('dafault'))}")
        print(f"About: {user_profile.get('about', user_profile.get('dafault'))}")
        print("\nExperiences:")

        if 'experience' in user_profile:
            for exp in user_profile['experience']:
                print(f"- Title: {exp['title']}")
                print(f"  Employer: {exp['employer']}")
                print(f"  Date Started: {exp['date_start']}")
                print(f"  Date Ended: {exp['date_end']}")
                print(f"  Location: {exp['location']}")
                print(f"  Description: {exp['description']}")
        else:
            print("No experiences provided.")

        print("\nEducation:")
        if 'education' in user_profile:
            for edu in user_profile['education']:
                print(f"- School: {edu['school']}")
                print(f"  Degree: {edu['degree']}")
                print(f"  Year Attended: {edu['year_attended']}")
        else:
            print("No education information provided.")
    else:
        print("You don't have a profile. Create one using 'create_profile'.")

def view_friend_profile(friend_username):
    with open('components/profile.json', 'r') as f:
        profiles = json.load(f)

    if friend_username in profiles:
        friend_profile = profiles[friend_username]

        print("\nFriend's Profile:")
        print(f"Title: {friend_profile.get('title', friend_profile.get('dafault'))}")
        print(f"Major: {friend_profile.get('major', friend_profile.get('dafault'))}")
        print(f"University: {friend_profile.get('university', friend_profile.get('dafault'))}")
        print(f"About: {friend_profile.get('about', friend_profile.get('dafault'))}")
        print("\nExperiences:")

        if 'experience' in friend_profile:
            for exp in friend_profile['experience']:
                print(f"- Title: {exp['title']}")
                print(f"  Employer: {exp['employer']}")
                print(f"  Date Started: {exp['date_start']}")
                print(f"  Date Ended: {exp['date_end']}")
                print(f"  Location: {exp['location']}")
                print(f"  Description: {exp['description']}")
        else:
            print("No experiences provided.")

        print("\nEducation:")
        if 'education' in friend_profile:
            for edu in friend_profile['education']:
                print(f"- School: {edu['school']}")
                print(f"  Degree: {edu['degree']}")
                print(f"  Year Attended: {edu['year_attended']}")
        else:
            print("No education information provided.")
    else:
        print("This friend does not have a profile.")

def profile():
    if not Config.FLAG:
        print("\nPlease log in to your account before see your profile and friends' profile.")
        login.login()
        return

    choice = None
    while choice != 4:
        print("\n1. View your profile\n2. Create/Update your profile\n3. View a friend's profile\n4. Quit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            view_profile(Config.SYSTEM_ACCOUNT[0])
        elif choice == 2:
            create_profile(Config.SYSTEM_ACCOUNT[0])
        elif choice == 3:
            with open('components/friendLists.json', 'r') as f:
                friendlists = json.load(f)
            print("Your friends are: ")
            for user in friendlists:
                if Config.SYSTEM_ACCOUNT[2] in user:
                    user_id = friendlists.index(user)
                    for i in range(len(user[Config.SYSTEM_ACCOUNT[2]]['friendList'])):
                        print(f'{i}. {user[Config.SYSTEM_ACCOUNT[2]]["friendList"][i]}')
            friend_choice = int(input("Enter the username of the friend whose profile you want to view: "))
            friend_username = friendlists[user_id][Config.SYSTEM_ACCOUNT[2]]['friendList'][friend_choice]
            view_friend_profile(friend_username)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
