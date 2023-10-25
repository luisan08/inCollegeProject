import pandas as pd
import numpy as np
import json
from components.config import Config
import components.login as login

accounts = pd.read_csv('components/accounts.csv')
with open('components/jobs.json', 'r') as f:
    jobs = json.load(f)

def jobPosting_attempts(attempts = 10):
    return len(jobs) >= attempts

def jobSearch():

    global accounts 
    global jobs

    while True:
        print("Welcome to the Job Search! Choose a number for the options below")
        print("1. Post a Job")
        print("2. Delete a Job")
        print("3. Return to Job Search")
        
        option = int(input("Select your option: "))

        if option == 1:

            if jobPosting_attempts():
                print("All permitted jobs have been created, please come back later.")
                continue

            print("Enter the information for the job you would like to post!")
            jobTitle = input("Title: ")
            jobDescription = input("Description: ")
            jobEmployer = input("Employer: ")
            jobLocation = input("Location: ")
            jobSalary = input("Salary: ")

            username = Config.SYSTEM_ACCOUNT[2]
            job_id = np.random.randint(0, 100)
            while job_id in jobs:
                job_id = np.random.randint(0, 100)
            jobPosting = {
                'job_id' : job_id,
                'username': username,
                'Title': jobTitle,
                'Description': jobDescription,
                'Employer': jobEmployer,
                'Location': jobLocation,
                'Salary': jobSalary,
                'Applicants': []
            }

            jobs.append(jobPosting)
            with open('components/jobs.json', 'w') as f:
                json.dump(jobs, f, indent=4)

            print("You have successfully posted a job!")    

        elif option == 2:
            job_postings = []
            for job in jobs:
                if Config.SYSTEM_ACCOUNT[2] == job['username']:
                    job_postings.append(job)
            if len(job_postings) == 0:
                print("You have not posted any jobs.\n")
            else:
                for i, job in enumerate(job_postings):
                    print(f"{i}. {job['Title']}")
                choice = int(input("Select a job to delete: "))
                for job in jobs:
                    if Config.SYSTEM_ACCOUNT[2] == job['username'] and job['Title'] == job_postings[choice]['Title']:
                        jobs.remove(job)
                        print("You have successfully deleted a job!\n")    
                        break
        elif option == 3:
            print("Returning to Job Search.")
            break

        else:
            print("Invalid option. Please try again.")

def applyJob():
    if len(jobs) == 0:
        print("There are no jobs available to apply for.\n")
        return
    for job in jobs:
        print('--------------------------------------------------')
        if Config.SYSTEM_ACCOUNT[2] in job['Applicants']:
            print(f"{job['job_id']}. {job['Title']} (Applied)")
        else:
            print(f"{job['job_id']}. {job['Title']}")
        print(f"Description: {job['Description']}")
        print(f"Employer: {job['Employer']}")
        print(f"Location: {job['Location']}")
        print(f"Salary: {job['Salary']}")
        print('--------------------------------------------------')
        
    choice = int(input("Select a job to apply for: "))
    for job in jobs:
        if job['job_id'] == choice:
            if Config.SYSTEM_ACCOUNT[2] in job['Applicants']:
                print("You have already applied for this job.\n")
                return
            if job['username'] == Config.SYSTEM_ACCOUNT[2]:
                print("You cannot apply for your own job.\n")
                return
            application = {}
            application['username'] = Config.SYSTEM_ACCOUNT[2]
            application['graduation_date'] = input("Enter your graduation date (mm/dd/yyyy): ")
            application['start_working_date'] = input("Enter a day you can start working (mm/dd/yyyy): ")
            application['paragraph'] = input("Enter a paragraph why you are a good fit for this job: ")
            job['Applicants'].append(application)
            print("You have successfully applied for a job!\n")    
            with open('components/jobs.json', 'w') as f:
                json.dump(jobs, f, indent=4)
            return

def saveJob():
    pass
    # for job in jobs:
    #     print('--------------------------------------------------')
    #     if Config.SYSTEM_ACCOUNT[2] in job['Applicants']:
    #         print(f"{job['job_id']}. {job['Title']} (Saved)")
    #     else:
    #         print(f"{job['job_id']}. {job['Title']}")
    #     print(f"Description: {job['Description']}")
    #     print(f"Employer: {job['Employer']}")
    #     print(f"Location: {job['Location']}")
    #     print(f"Salary: {job['Salary']}")
    #     print('--------------------------------------------------')
        
    # choice = int(input("Select a job to save: "))
    # for job in jobs:
    #     if job['job_id'] == choice:
    #         if Config.SYSTEM_ACCOUNT[2] in job['Applicants']:
    #             print("You have already saved this job.\n")
    #             return
    #         if job['username'] == Config.SYSTEM_ACCOUNT[2]:
    #             print("You cannot save your own job.\n")
    #             return
    #         job['Applicants'].append(Config.SYSTEM_ACCOUNT[2])
    #         print("You have successfully saved a job!\n")    
    #         with open('components/jobs.json', 'w') as f:
    #             json.dump(jobs, f, indent=4)
    #         return

def skillSearch():
    print("Welcome to Skill Learner! Which skill are you interested in learning?")
    # available skills are listed, skills are placeholders atm
    print("1. Communication Skills\n2. Teamwork Skills\n3. Interpersonal Skills\n4. Learning/Adaptability Skills\n5. Self-management Skills\n6. Return to search")
    skillChoice = int(input("Please select by inputting the corresponding number: "))

    while True: #input validation
        if skillChoice == 1: 
            print("Under construction.")
            break
        if skillChoice == 2:
            print("Under construction.")
            break
        if skillChoice == 3:
            print("Under construction.")
            break
        if skillChoice == 4:
            print("Under construction.")
            break
        if skillChoice == 5:
            print("Under construction.")
            break
        if skillChoice == 6:
            search()
            break
        else: 
            # user can only enter valid option
            skillChoice = int(input("Invalid choice. Please input a number corresponding with your desired skill: ")) 
        return
        
# search is the main search function where other searches can be selected
def search(): 
    if not Config.FLAG:
            print("\nPlease log in to your account before searching for jobs")
            login.login()
            return

    while True: #input validation
        print("\nSearch Options:\n1. Post/Delete Jobs\n2. Apply/Save Jobs\n3. Learn a Skill\n3. Quit Search")
        searchChoice = int(input("Please enter your desired search: "))
        if searchChoice == 1: 
            jobSearch()
        elif searchChoice == 2:
            print("1. Apply for a job\n2. Save a job\n3. Return to Job Search")
            choice = int(input("Select your option: "))
            if choice == 1:
                applyJob()
            elif choice == 2:
                saveJob()
            else:
                print("Invalid option. Please try again.")
        elif searchChoice == 3:
            skillSearch()
        elif searchChoice == 4: # quit search
            break
        else: 
            searchChoice = int(input("Invalid choice. Please input a number corresponding with your desired search."))
    return
        
