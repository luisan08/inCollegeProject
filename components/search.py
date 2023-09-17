#jobSearch allows user to search for jobs
def jobSearch(): 
    print("Under construction.")
    return

#jobSearch allows people to find people they know
def peopleSearch():
    print("Under construction.")
    return

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
    print("Search Options:\n1. Look for Jobs\n2. Find People You Know\n3. Learn a Skill\n4. Quit Search")
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
        


   
    