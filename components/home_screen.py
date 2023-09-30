from components.login import in_InCollege_System

def home_screen():
    print( 
            """
            ************************************************************
            *                 Student Success Story                    *
            ************************************************************
            """
            )
    print()
    print("""\tAshkan Fakhrtabatabaie is studying Music Composition. He has a passion for music and spends most of his time composing music and studying or teaching music theory and technology. Ashkan has been able to thrive as a composer in part by utilizing his background in engineering. He enjoys thinking in an interdisciplinary way, making connections, creating bridges between realms. Since coming to the University of Utah, he has written a handful of pieces and had the fortune of having his music and scholarly works published or performed at a number of music festivals, including last summer at the New York City Electroacoustic Music Festival (NYCEMF) and this year at the Missouri Experimental Sonic Arts Festival (MOXsonic\
Ashkan describes having grown immensely from his work with professors here at the U.\n In fact it was one of his professors in the School of Music who advised him to reach out to Student Success Advocate Lisa Lewis for help looking for a summer job utilizing his expertise in music composition. Ashkan had no idea if such jobs even existed or what to do to find one.\
Once Lisa understood Ashkan’s interest, she and a colleague in the Union Administrative Office began brainstorming possible job opportunities with the Union over the summer.\n It turned out that the Union actually needed the services of a multi-media producer and hired Ashkan to compile digital images and make music for videos.\n The job gave Ashkan a great opportunity to apply his knowledge of art and technology in a commercial way. In his words, “Most of the time in art school, projects are just for the sake of art, but this job required me to apply my skills and talent to a real life project.\
If Ashkan were to give advice to other students, he would tell them, “Don’t be hesitant about acknowledging the skills you have. Maybe you will be able to find something that you will be good at and even create a job position that benefits both you and your employer!""")
    print()


    while True:

        print("\nNavigation")
        print("1. Watch a Video")
        print("2. Find Friends in the InCollege System")
        print("3. Continue with Menu")
        
        option = int(input("Select an option: "))

        if option == 1:
            choice = input("Would you like to play a video we made for you? (y/n): ")
            if choice == "y":
                print("\nVideo is now playing\n")
            else:
                print("That's ok, you can watch it later.")

        elif option == 2:
            in_InCollege_System()

        elif option == 3:
            break 

        else:
            print("Invalid option. Try again.")
