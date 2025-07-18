import os

USER_FILE = 'data/users.txt'

# Add User
def add_user():
    from modules.admin import manage_staff
    print("═" * 50)
    print("add new staff".center(50).upper())
    print("═" * 50)
    try:
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = f"{username}@123"
        user_role = input("Enter your role: ")
        if os.path.exists(USER_FILE):
            with open(USER_FILE, "r") as file:
                for line in file:
                    if line.strip().split(",")[0] == username:
                        raise Exception(f"'{username}' is already added.")

        with open(USER_FILE, "a") as file:
            file.write(f"{username},{email},{password},{user_role}\n")
        print("Added new user successfully.")
    except Exception as error:
        print(error)
    manage_staff()

# View Staff
def view_staff():
    from modules.admin import manage_staff, admin_interface
    print("\n" + "═" * 50)
    print("view all staff".upper().center(50))
    print("═" * 50)
    user_number = 1
    file = open(USER_FILE, 'r')
    for line in file:
        username, email, password, role = line.strip().split(",")
        if role in ("manager", "chef"):
            print(f"{user_number}. Username: {username}, Email: {email} User Role: {role}")
            user_number += 1

    print("\n" + "═" * 50)
    print("1. Back to Manage Staff Interface")
    print("2. Back to Admin Panel")
    choose_option = int(input("Enter your choice: "))
    match choose_option:
        case 1:
            manage_staff()
        case 2:
            print("\n" + "═" * 50)
            admin_interface()

# Update User Profile