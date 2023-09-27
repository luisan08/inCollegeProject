from components.welcome import welcome
from components.home_screen import home_screen
from components.login import in_InCollege_System
from components.search import search
from components.menu import general_menu


def main():
    welcome()
    home_screen()
    in_InCollege_System()
    general_menu()
    search()


if __name__ == "__main__":
    main()