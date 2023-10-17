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
    experience = {}
    for i in range(num_of_experience):
        experienceID = 'experience' + str(i)
        experience[experienceID] = {}
        experience[experienceID]['title'] = input('Title of Experience: ')
        experience[experienceID]['employer'] = input('Employer: ')
        experience[experienceID]['date_start'] = input('Date Started: ')
        experience[experienceID]['date_end'] = input('Date Ended: ')
        experience[experienceID]['location'] = input('Location: ')
        experience[experienceID]['description'] = input('Description: ')

    num_of_education = int(input('Number of Education you have: '))
    education = {}
    for i in range(num_of_education):
        educationID = 'education' + str(i)
        education[educationID] = {}
        education[educationID]['school'] = input('School: ')
        education[educationID]['degree'] = input('Degree: ')
        education[educationID]['year_attended'] = input('Year Attended: ')

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
