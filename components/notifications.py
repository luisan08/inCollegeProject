import json
from components.config import Config


with open('components/jobs.json', 'r') as f:
    jobs = json.load(f)

with open('components/profile.json', 'r') as file:
        profiles = json.load(file)

with open('components/friendLists.json', 'r') as file:
        messages = json.load(file)


def check_and_display_notifications(username):

    print("\nNotifications!")
    print("----------------------------------------------------")

    #notification for profiles    
    if username not in profiles:
        print("\nDon't forget to create a profile.")

    #message 
    for message in messages:
        if message.get(username):
            inbox = message[username].get('inbox', [])
            unread_messages = [msg for msg in inbox if not msg.get('read')]
            for msg in unread_messages:
                print(f"\nYou have a new messages waiting for you ")

def reminder_jobs(username):
     
    applied_jobs = [job for job in jobs if username in [applicant.get('username') for applicant in job['Applicants']]]

    # Check if the student has any recent job applications
    recent_applications = [job for job in applied_jobs if job['Applicants'][0]['username'] == username]
    num_jobs = notify_applied_jobs
    if not recent_applications or num_jobs == 0:
        print("\nRemember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")


#notifications for job section
def notify_applied_jobs(username):
    applied_jobs = [job for job in jobs if username in [applicant.get('username') for applicant in job['Applicants']]]
    num_applied_jobs = len(applied_jobs)
    print(f"\nYou have currently applied for {num_applied_jobs} job{'s' if num_applied_jobs != 1 else ''}.")
    return num_applied_jobs



def deleted_job(username):

    if username in profiles and 'jobDelete_noti' in profiles[username]:
        deleted_jobs_notifications = profiles[username]['jobDelete_noti']

        for job_id, job_title in deleted_jobs_notifications:
            print(f"A job that you applied for has been deleted:")
            print(f"  Job Title: {job_title}")
          

        # Clear the deleted job notifications
        profiles[username]['jobDelete_noti'] = []

