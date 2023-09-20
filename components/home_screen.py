def home_screen():
    print( 
            """
            ************************************************************
            *                 Student Success Story                    *
            ************************************************************
            """
            )
    print()
    print("I am a senior in Computer Science and I am looking for a job in the tech industry.")

    choice = input("Would you like to play a video we made for you? (y/n): ")
    if choice == "y":
        print("\nVideo is now playing\n")
    else:
        print("That's ok, you can watch it later.")