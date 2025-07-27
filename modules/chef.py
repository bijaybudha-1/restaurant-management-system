from modules.crud import update_profile

FILE_NAME = 'data/users.txt'
MENU_FILE = 'data/menu.txt'

def update_chef_profile(username):
    update_profile(username)
    chef_menu(username)

def chef_menu(username):
    from modules.auth import auth_interface
    print("\n" + "═" * 50)
    print("Chef Menu".center(50))
    print("═" * 50)
    print("1. View Order")
    print("2. Update Orders Status")
    print("3. Update Profile")
    print("4. Logout (Exit)")
    choose_number = int(input("Enter your choice: "))
    match choose_number:
        case 1:
            print("view Orders")
        case 2:
            print("Update Orders Status")
        case 3:
            update_chef_profile(username)
        case 4:
            auth_interface()


def chef_interface(username):
    print(f"{username.capitalize()}, Welcome to the Restaurant Management System!")
    chef_menu(username)
