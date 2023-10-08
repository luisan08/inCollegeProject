import pandas as pd
from components.config import Config
import components.login as login

accounts = pd.read_csv('components/accounts.csv')
accounts_jobs = pd.read_csv('components/accounts_jobs.csv')

#jobSearch allows user to search for jobs
def jobPosting_attempts(attempts = 5):
    return len(accounts_jobs) >= attempts

def jobSearch():

    global accounts 
    global accounts_jobs

    while True:
        print("Welcome to the Job Search! Choose a number for the options below")
        print("1. Post a Job")
        print("2. Return to Job Search")
        
        option = int(input("Select your option:"))

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

            account = Config.SYSTEM_ACCOUNT or ['Default First Name', 'Default Last Name']

            jobPosting = {
                'Title': [jobTitle],
                'Description': [jobDescription],
                'Employer': [jobEmployer],
                'Location': [jobLocation],
                'Salary': [jobSalary],
                'First': account[0],
                'Last': account[1]
            }

            jobPosting = pd.DataFrame(jobPosting, index=[0])
            accounts_jobs = pd.concat([accounts_jobs, jobPosting], ignore_index=True)
            accounts_jobs.to_csv('components/accounts_jobs.csv', index=False)
            
            print("You have successfully posted a job!")    
            print("\n")

        elif option == 2:
            print("Returning to Job Search.")
            break

        else:
            print("Invalid option. Please try again.")

#peopleSearch allows people to find people they know
def peopleSearch():

    global accounts 
    while True:
        print("Find people you know! Choose a number for the options below")
        print("1. Search for people ")
        print("2. Return to People Search")
        option = int(input("Select your option:"))
    
        if(option == 1):

            first = input("Enter the first name: ")
            last = input("Enter the last name: ")
     
            if (first, last) in zip(accounts['first'], accounts['last']):
                print("Would you like to connect with", first, last, "?")
            else:
                print("Username was not found.")
                print("\n")
        
        elif option == 2:
            print("Returning to People Search.")
            break 

        else:
            print("Invalid option. Returning to People Search.") 


#skillSearch allows users to choose to learn a skill from a list
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
    print("\nSearch Options:\n1. Look for Jobs\n2. Find People You Know\n3. Learn a Skill\n4. Quit Search")
    searchChoice = int(input("Please enter your desired search: "))

    while True: #input validation
        if searchChoice == 1: 
            jobSearch()
            break
        elif searchChoice == 2:
            peopleSearch()
            break
        elif searchChoice == 3:
            skillSearch()
            break
        elif searchChoice == 4: # quit search
            break
        else: 
            # user can only enter valid option
            searchChoice = int(input("Invalid choice. Please input a number corresponding with your desired search.\n"))
    return
        
