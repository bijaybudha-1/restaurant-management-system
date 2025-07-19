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

# Update Profile
def update_profile(verify_username):
    print("\n" + "═" * 50)
    print("UPDATE Profile".center(50))
    print("═" * 50)

    if not os.path.exists(USER_FILE):
        print("User file not found.".center(50))
        return

    updated_lines = []
    user_found = False

    with open(USER_FILE, "r") as file:
        for line in file:
            username, email, password, role = line.strip().split(",")

            if username == verify_username:
                print(f"User '{username}' found. Leave blank to keep current value.")
                print("─" * 50)

                new_username = input(f"Enter your new username: ").strip() or username
                new_email = input(f"Enter your new email: ").strip() or email
                new_password = input(f"Enter your new password [****]: ").strip() or password

                updated_line = f"{new_username},{new_email},{new_password},{role}\n"
                updated_lines.append(updated_line)
                user_found = True
            else:
                updated_lines.append(line)

    print("\n" + "═" * 50)
    if user_found:
        with open(USER_FILE, "w") as file:
            file.writelines(updated_lines)
        print("Profile updated successfully.".capitalize().center(50))
    else:
        print("Username not found.")
    print("═" * 50 + "\n")


# Update User Profile
