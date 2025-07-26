import os

from modules.crud import update_profile, add_user, view_chef_customer

MENU_FILE = 'data/menu.txt'

def add_customer():
    add_user()

def manage_customer(username):
    print("\n" + "═" * 50)
    print("Manage Chef and Customer Panel".center(50))
    print("═" * 50)
    print("1. Add New Chef or Customer")
    print("2. View Chef or Customer")
    print("3. Update Chef or  Customer")
    print("4. Delete Chef or Customer")
    print("5. Back to Manager Main Panel")
    choose_number = int(input("Enter your choice: "))
    match choose_number:
        case 1:
            add_customer()
        case 2:
            view_chef_customer(username)
        case 3:
            print("Update Customer")
        case 4:
            print("Delete Customer")
        case 5:
            print("Back to Manager Main Panel")



def manager_update_profile(username):
    update_profile(username)
    manager_interface(username)

def manager_interface(username):
    print(f"{username}, Welcome to the Restaurant Management System!")
    manager_panel(username)

def manager_panel(username):
    print("Manager Main Panel".center(50))
    print("═" * 50)
    print("1. Manage Customers")
    print("2. Manage Menu")
    print("3. Update Profile")
    print("4. Logout (Exit)")
    choose_number = int(input("Choose an option: "))
    match choose_number:
        case 1:
            manage_customer(username)
        case 2:
            print("Manage Menu")
        case 3:
            manager_update_profile(username)
        case 4:
            print("4. Logout (Exit)")

def add_food():
    print("\n" + "═" * 50)
    print("Add New Food".center(50))
    print("═" * 50)
    food_name = input("Enter food item name: ")
    price = input("Enter food price: ")

    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, "r") as file:
            for line in file:
                if line.strip().split(",")[0] == food_name:
                    print(f"{food_name} is already Added.")
                    return

    with open(MENU_FILE, "a") as file:
        file.write(f"{food_name},{price}\n")
    print("Added new food successfully.")

