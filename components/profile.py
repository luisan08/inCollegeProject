import json
from components.config import Config
import string

def create_profile():
    with open('components/profile.json', 'r') as f:
        profiles = json.load(f)

    title = input('Enter a title for your profile: ')
    major = string.capwords(input('Enter your major: '))
    university = string.capwords(input('Enter the University you attend currently: '))
    about = input('Describe yourself: ')

    #experience section
    num_of_experience = int(input('How much previous work experience do you have? (Up to 3 previous jobs) '))
    while num_of_experience > 3 or num_of_experience < 0: #input validation
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

    #education section
    num_of_education = int(input('How many higher level institutions have you attended? '))
    while num_of_education < 1: #input validation
        num_of_education = int(input('Number must be 1 or greater. Please try again: '))

    education = []
    for i in range(num_of_education):
        new_education = {}
        new_education['school'] = string.capwords(input('School: '))
        new_education['degree'] = string.capwords(input('Degree: '))
        new_education['year_attended'] = input('Years Attended: ')
        education.append(new_education)

    SYSTEM_ACCOUNT = ['user_profile']

    username = SYSTEM_ACCOUNT[0]

    profiles[username] = {}
    profiles[username]['title'] = title
    profiles[username]['major'] = major
    profiles[username]['university'] = university
    profiles[username]['about'] = about
    profiles[username]['experience'] = experience
    profiles[username]['education'] = education


    with open('components/profile.json', 'w') as f:
        json.dump(profiles, f, indent=4)

def view_profile(username):
    with open('components/profile.json', 'r') as f:
        profiles = json.load(f)

    if username in profiles:
        user_profile = profiles[username]

        print("\nUser Profile:")
        print(f"Title: {user_profile['title']}")
        print(f"Major: {user_profile['major']}")
        print(f"University: {user_profile['university']}")
        print(f"About: {user_profile['about']}")
        print("\nExperiences:")
        for exp in user_profile['experience']:
            print(f"- Title: {exp['title']}")
            print(f"  Employer: {exp['employer']}")
            print(f"  Date Started: {exp['date_start']}")
            print(f"  Date Ended: {exp['date_end']}")
            print(f"  Location: {exp['location']}")
            print(f"  Description: {exp['description']}")
        print("\nEducation:")
        for edu in user_profile['education']:
            print(f"- School: {edu['school']}")
            print(f"  Degree: {edu['degree']}")
            print(f"  Year Attended: {edu['year_attended']}")
    else:
        print("You don't have a profile. Create one using 'create_profile'.")

def view_friend_profile(username, friend_username):
    with open('components/profile.json', 'r') as f:
        profiles = json.load(f)

    if friend_username in profiles:
        friend_profile = profiles[friend_username]

        print("\nFriend's Profile:")
        print(f"Title: {friend_profile['title']}")
        print(f"Major: {friend_profile['major']}")
        print(f"University: {friend_profile['university']}")
        print(f"About: {friend_profile['about']}")
        print("\nExperiences:")
        for exp in friend_profile['experience']:
            print(f"- Title: {exp['title']}")
            print(f"  Employer: {exp['employer']}")
            print(f"  Date Started: {exp['date_start']}")
            print(f"  Date Ended: {exp['date_end']}")
            print(f"  Location: {exp['location']}")
            print(f"  Description: {exp['description']}")
        print("\nEducation:")
        for edu in friend_profile['education']:
            print(f"- School: {edu['school']}")
            print(f"  Degree: {edu['degree']}")
            print(f"  Year Attended: {edu['year_attended']}")
    else:
        print("This friend does not have a profile.")

if __name__ == "__main__":
    create_profile("user_profile")  # Replace "user_profile" with the actual username of the user
    view_profile("user_profile")
