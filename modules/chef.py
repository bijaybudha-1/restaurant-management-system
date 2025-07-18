import os

FILE_NAME = 'data/users.txt'
MENU_FILE = 'data/menu.txt'

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

    # update_profile()


def chef_interface(username):
    print(f"{username.capitalize()}, Welcome to the Restaurant Management System!")
    add_food()