import json
from config import Config

def create_profile():
    with open('components/profile.json', 'r') as f:
        profiles = json.load(f)

    title = input('Title (such as 3rd Student Computer Science): ')
    major = input('Major (such as Computer Science): ')
    university = input('University (such as University of California): ')
    description = input('Description (such as I am an aspiring SWE): ')
    num_of_experience = int(input('Number of Experiences you have: '))
    experience = []
    for i in range(num_of_experience):
        new_experience = {}
        new_experience['title'] = input('Title of Experience: ')
        new_experience['employer'] = input('Employer: ')
        new_experience['date_start'] = input('Date Started: ')
        new_experience['date_end'] = input('Date Ended: ')
        new_experience['location'] = input('Location: ')
        new_experience['description'] = input('Description: ')
        experience.append(new_experience)

    num_of_education = int(input('Number of Education you have: '))
    education = []
    for i in range(num_of_education):
        new_education = {}
        new_education['school'] = input('School: ')
        new_education['degree'] = input('Degree: ')
        new_education['year_attended'] = input('Year Attended: ')
        education.append(new_education)

    # FOR DEMO ONLY
    SYSTEM_ACCOUNT = ['hieung']

    username = SYSTEM_ACCOUNT[0]

    profiles[username] = {}
    profiles[username]['title'] = title
    profiles[username]['major'] = major
    profiles[username]['university'] = university
    profiles[username]['description'] = description
    profiles[username]['experience'] = experience
    profiles[username]['education'] = education


    with open('components/profile.json', 'w') as f:
        json.dump(profiles, f, indent=4)

# FOR DEMO ONLY
create_profile()
