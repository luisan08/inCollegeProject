from components.welcome import welcome
from components.home_screen import home_screen
from components.login import in_InCollege_System
from components.search import search
from components.menu import general_menu
from components.config import Config



def main():

    welcome()
    home_screen()
    in_InCollege_System()
    general_menu()
    if Config.FLAG == True:
        search()


if __name__ == "__main__":
    main()