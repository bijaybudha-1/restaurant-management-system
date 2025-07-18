import  os
from modules.menu import view_order_menu

FILE_USER = 'data/users.txt'
FILE_MENU = 'data/menu.txt'

def update_profile():
    update_user_profile()

def send_feedback():
    print("\n" + "═" * 50)
    print("Please drop your feedback below.".upper().center(50))
    print("═" * 50)

def update_user_profile():
    print("\n" + "═" * 50)
    print("USER PROFILE UPDATE".center(50))
    print("═" * 50)
    username_to_update = input("Enter your current username: ").strip()

    if not os.path.exists(FILE_USER):
        print("User file not found.".title().center(50))
        return

    updated_lines = []
    user_found = False

    with open(FILE_USER, "r") as file:
        for line in file:
            username, email, password, role = line.strip().split(",")

            if username == username_to_update:
                print("\n" + "─" * 50)
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
        with open(FILE_USER, "w") as file:
            file.writelines(updated_lines)
        print("Profile updated successfully.".title().center(50))
    else:
        print("Username not found.")
    print("═" * 50 + "\n")

def customer_interface(username):
    print("\n" + "═" * 50)
    print("Customer Menu".center(50))
    print(f"{username.capitalize()}, Welcome to our Restaurant ".upper().center(50))
    print("═" * 50)
    print("1. View & Order Food")
    print("2. Send Feedback")
    print("3. Update profile")
    print("4. Cancel")
    user_selected = int(input("Enter your choice: "))
    match user_selected:
        case 1:
            view_order_menu()
        case 2:
            send_feedback()
        case 3:
            update_user_profile()
        case 4:
            exit()