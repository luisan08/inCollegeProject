import json

with open('components/jobs.json', 'r') as f:
    jobs = json.load(f)

with open('components/profile.json', 'r') as file:
        profiles = json.load(file)

with open('components/friendLists.json', 'r') as file:
        messages = json.load(file)

#notifications for  messages - reuse function

def check_and_display_notifications(username):

    print("\nNotifications!")
    print("----------------------------------------------------")

    applied_jobs = [job for job in jobs if username in [applicant.get('username') for applicant in job['Applicants']]]
    
    # Check if the student has not applied for a job in the past 7 days
    recent_applications = [job for job in applied_jobs if job['Applicants'][0]['username'] == username and job['Applicants'][0]['start_working_date'] == "05/28/2023"]
    
    if not recent_applications:
        print("\nRemember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
    
    #job deletetion - do we have one already?
    deleted_jobs = [job for job in applied_jobs if job['Title'] not in [job['Title'] for job in jobs]]

    for job in deleted_jobs:
        print(f"\nA job that you applied for has been deleted: {job['Title']}")

    #notification for profiles    
    if username not in profiles:
        print("\nDon't forget to create a profile.")
    

    #new job posted


#notifications for job section
def notify_applied_jobs(username):
    applied_jobs = [job for job in jobs if username in [applicant.get('username') for applicant in job['Applicants']]]
    num_applied_jobs = len(applied_jobs)
    print(f"\nYou have currently applied for {num_applied_jobs} job{'s' if num_applied_jobs != 1 else ''}.")


#notifications when somone joins 
def check_and_display_new_student_notification(username, accounts, new_student_notifications):
    student_account = next((account for account in accounts if account['username'] == username), None)
    
    if student_account and student_account['first'] and student_account['last'] and username in new_student_notifications:
        first_name = student_account['first']
        last_name = student_account['last']
        print(f"\n{first_name} {last_name} has joined InCollege.")
        # Mark the notification as sent
        new_student_notifications.remove(username)