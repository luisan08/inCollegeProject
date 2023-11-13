import json
from components.config import Config
from datetime import datetime


with open('components/jobs.json', 'r') as f:
    jobs = json.load(f)

with open('components/profile.json', 'r') as file:
    profiles = json.load(file)

with open('components/friendLists.json', 'r') as file:
    messages = json.load(file)

# notification for no profile
def no_profile_notif(username):  
    if username not in profiles:
        print("\nDon't forget to create a profile.")

# notification for new messages
def message_notif(username):
    #message 
    for message in messages:
        if message.get(username):
            inbox = message[username].get('inbox', [])
            unread_messages = [msg for msg in inbox if not msg.get('read')]
            for msg in unread_messages:
                print(f"\nYou have a new messages waiting for you ")

# notification for when a user has not applied to any job for the last 7 days
def reminder_jobs(username):
    hasApplied = False

    # Check if the user has applied for any job for the last 7 days
    for job in jobs:
        for applicant in job["Applicants"]:
            if applicant["username"] == username:
                if (datetime.now() - datetime.strptime(applicant["appliedDate"], "%m/%d/%Y")).days <= 7: return
                else: hasApplied = True

    if hasApplied:
        print('Remember – you\'re going to want to have a job when you graduate. Make sure that you start to apply for jobs today!')


#notification for job section
def notify_applied_jobs(username):
    applied_jobs = [job for job in jobs if username in [applicant.get('username') for applicant in job['Applicants']]]
    num_applied_jobs = len(applied_jobs)
    print(f"\nYou have currently applied for {num_applied_jobs} job{'s' if num_applied_jobs != 1 else ''}.")
    return num_applied_jobs

#notification for job deletion
def deleted_job(username):
    with open('components/notifications.json', 'r') as f:
        notifications = json.load(f)
    
    if username in notifications:
        for job in notifications[username]["deletedJobs"]:
            print(f"\nThe job named {job} that you applied for has been deleted.")

# notification for a new posted job          
def new_job(username):
    if jobs:
        last_job = jobs[-1]
        if username not in [applicant['username'] for applicant in last_job['Applicants']]:
            job_title = last_job['Title']
            print(f"\nA new job '{job_title}' has been posted.")


def new_student(username):
    with open('components/notifications.json', 'r') as f:
        notifications = json.load(f)
    
    if "student" in notifications[username]:
        for newUser in notifications[username]["student"]:
            print(f"{newUser['first']} {newUser['last']} has joined InCollege.")
    
        notifications[username]["student"] = []
    
    with open('components/notifications.json', 'w') as f:
        json.dump(notifications, f, indent=4)


