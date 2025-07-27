import os

USER_FILE = 'data/users.txt'
MENU_FILE = 'data/menus.txt'

# Admin Add User
def admin_add_user(stored_username):
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
            print("\n" + "-" * 50)
        print("Added new user successfully.")
        print("-" * 50)
    except Exception as error:
        print("\n" + "-" * 50)
        print(error)
        print("-" * 50)
    manage_staff(stored_username)

# View Staff
def view_staff(stored_username):
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
            manage_staff(stored_username)
        case 2:
            print("\n" + "═" * 50)
            admin_interface(stored_username)

# Update Profile
def update_profile(verify_username):
    print("\n" + "═" * 50)
    print("UPDATE Profile".center(50))
    print("═" * 50)

    if not os.path.exists(USER_FILE):
        print("\n" + "-" * 50)
        print("User file not found.".center(50))
        print("-" * 50)
        return

    updated_lines = []
    user_found = False

    with open(USER_FILE, "r") as file:
        for line in file:
            username, email, password, role = line.strip().split(",")

            if username == verify_username:
                print("\n" + "-" * 50)
                print(f"User '{username}' found. Leave blank to keep current value.".center(50))
                print("-" * 50)

                new_username = input(f"Enter your new username: ").strip() or username
                new_email = input(f"Enter your new email: ").strip() or email
                new_password = input(f"Enter your new password [****]: ").strip() or password

                updated_line = f"{new_username},{new_email},{new_password},{role}\n"
                updated_lines.append(updated_line)
                user_found = True
            else:
                updated_lines.append(line)

    print("\n" + "-" * 50)
    if user_found:
        with open(USER_FILE, "w") as file:
            file.writelines(updated_lines)
        print("Profile updated successfully.".capitalize().center(50))
    else:
        print("Username not found.")
    print("-" * 50)


# Update User Profile
def update_user_profile(stored_username):
    from modules.admin import manage_staff, admin_interface
    print("\n" + "═" * 60)
    print("USER PROFILE UPDATE".center(60))
    print("═" * 60)
    username_to_update = input("Enter the updated username for the staff member: ").strip()

    if not os.path.exists(USER_FILE):
        print("\n" + "-" * 50)
        print("User file not found.".center(50))
        print("-" * 50)
        return

    updated_lines = []
    user_found = False

    with open(USER_FILE, "r") as file:
        for line in file:
            username, email, password, role = line.strip().split(",")

            if username == username_to_update:
                print("\n" + "-" * 50)
                print(f"User '{username}' found. Leave blank to keep current value.".center(50))
                print("─" * 50)

                new_username = input(f"Enter your new username: ").strip() or username
                new_email = input(f"Enter your new email: ").strip() or email
                new_role = input(f"Enter your new role: ").strip() or role

                updated_line = f"{new_username},{new_email},{password},{new_role}\n"
                updated_lines.append(updated_line)
                user_found = True
            else:
                updated_lines.append(line)

    print("\n" + "-" * 50)
    if user_found:
        with open(USER_FILE, "w") as file:
            file.writelines(updated_lines)
        print("Profile updated successfully.".capitalize().center(50))
        print("-" * 50)
        print("1. Back to Manage Staff Interface")
        print("2. Back to Admin Panel")
        choose_option = int(input("Enter your choice: "))
        match choose_option:
            case 1:
                manage_staff(stored_username)
            case 2:
                print("═" * 50)
                admin_interface(stored_username)
    else:
        print("Username not found.")
    print("-" * 50)

# Delete User Profile
def delete_user_profile():
    from modules.admin import manage_staff, admin_interface
    print("\n" + "═" * 50)
    print("Delete Staff Profile".center(50))
    print("═" * 50)
    removed_username = input("Enter the username to remove: ").strip()

    try:
        with open(USER_FILE, "r") as file:
            lines = file.readlines()

        user_found = False
        deleted = False

        with open(USER_FILE, "w") as file:
            for line in lines:
                username, email, password, role = line.strip().split(",")

                if username == removed_username:
                    user_found = True
                    if role.lower() in ["manager", "chef"]:
                        deleted = True
                        continue  # Skip writing this line to delete
                    else:
                        print("\n" + "-" * 60)
                        print(f"Admin can only remove the data of users whose role is chef or manager")
                        print("-" * 60)
                        file.write(line)
                else:
                    file.write(line)

        if not user_found:
            print("-" * 50)
            print("Username not found.")
            print("-" * 50)
        elif deleted:
            print("\n" + "-" * 50)
            print(f"User '{removed_username}' has been deleted successfully.".center(50))
            print("-" * 50)

        try:
            choose_option = int(input("Choice a number 1 or 2: "))
            match choose_option:
                case 1:
                    manage_staff(None)
                case 2:
                    admin_interface(None)

        except ValueError:
            print("\n" + "-" * 50)
            print("Invalid input. Please enter a number.".center(50))
            print("-" * 50)


    except FileNotFoundError:
        print("\n" + "-" * 50)
        print("Error: User file not found.".center(50))
        print("-" * 50)

# Manager Crud Operation

# View Customer List
def view_customer(stored_username):
    from modules.manager import manage_customer, manager_panel
    print("\n" + "═" * 60)
    print("view all customer".upper().center(60))
    print("═" * 60)
    user_number = 1
    file = open(USER_FILE, 'r')
    for line in file:
        username, email, password, role = line.strip().split(",")
        if role in "customer":
            print(f"{user_number}. Username: {username}, Email: {email} User Role: {role}")
            user_number += 1

    print("\n" + "═" * 50)
    print("1. Manage Customer Panel")
    print("2. Back to Manager Main Panel")
    choose_option = int(input("Enter your choice: "))
    match choose_option:
        case 1:
            manage_customer(stored_username)
        case 2:
            print("═" * 50)
            manager_panel(stored_username)

# Adding New Customer
def add_customer(stored_username):
    from modules.manager import manage_customer
    print("═" * 50)
    print("add new customer".center(50).upper())
    print("═" * 50)
    try:
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = f"{username}@123"
        user_role = "customer"
        if os.path.exists(USER_FILE):
            with open(USER_FILE, "r") as file:
                for line in file:
                    if line.strip().split(",")[0] == username:
                        raise Exception(f"'{username}' is already added.".center(50))

        with open(USER_FILE, "a") as file:
            file.write(f"{username},{email},{password},{user_role}\n")
            print("\n" + "-" * 50)
        print("Added new user successfully.".center(50))
        print("-" * 50)
    except Exception as error:
        print("\n" + "-" * 50)
        print(error)
        print("-" * 50)
    manage_customer(stored_username)

# Update Customer Profile
def update_customer_profile(stored_username):
    from modules.manager import manage_customer
    import os

    print("\n" + "═" * 50)
    print("CUSTOMER PROFILE UPDATE".center(50))
    print("═" * 50)
    username_to_update = input("Enter the username of the customer to update: ").strip()

    if not os.path.exists(USER_FILE):
        print("\n" + "-" * 50)
        print("User file not found.".center(50))
        print("-" * 50)
        return

    updated_lines = []
    user_found = False

    with open(USER_FILE, "r") as file:
        for line in file:
            username, email, password, role = line.strip().split(",")

            if username == username_to_update:
                user_found = True
                if role.strip().lower() != "customer":
                    print("\n" + "-" * 70)
                    print(f"Permission denied: You can only update users with role 'customer'.".center(70))
                    print("-" * 70)
                    updated_lines.append(line)
                    continue

                print(f"User '{username}' found. Leave blank to keep current value.")
                print("─" * 60)

                new_username = input("Enter new username: ").strip() or username
                new_email = input("Enter new email: ").strip() or email
                new_role = role  # Managers cannot change the role itself

                updated_line = f"{new_username},{new_email},{password},{new_role}\n"
                updated_lines.append(updated_line)
                print("\n" + "-" * 50)
                print("Profile updated successfully.".center(50))
                print("-" * 50)
            else:
                updated_lines.append(line)

    if user_found:
        with open(USER_FILE, "w") as file:
            file.writelines(updated_lines)
    else:
        print("\n" + "-" * 50)
        print("Username not found.".center(50))
        print("-" * 50)

    manage_customer(stored_username)

# Delete Customer Profile
def delete_customer(stored_username):
    from modules.manager import manage_customer, manager_panel

    print("\n" + "═" * 50)
    print("Delete Customer Profile".center(50))
    print("═" * 50)
    removed_username = input("Enter the username to remove: ").strip()

    try:
        with open(USER_FILE, "r") as file:
            lines = file.readlines()

        user_found = False
        deleted = False

        with open(USER_FILE, "w") as file:
            for line in lines:
                username, email, password, role = line.strip().split(",")

                if username == removed_username:
                    user_found = True
                    if role.lower() in "customer":
                        deleted = True
                        continue  # Skip writing this line to delete
                    else:
                        print("\n" + "-" * 80)
                        print(f"Admin can only remove the data of users whose role is chef or manager".center(80))
                        print("-" * 80)
                        file.write(line)
                else:
                    file.write(line)

        if not user_found:
            print("\n" + "-" * 50)
            print("Username not found.".center(50))
            print("-" * 50)
        elif deleted:
            print("\n" + "-" * 50)
            print(f"User '{removed_username}' has been deleted successfully.".center(50))
            print("-" * 50)

        try:
            print("1. Back to Customer Panel")
            print("2. Back to Manager Main Panel")
            choose_option = int(input("Choice a number 1 or 2: "))
            match choose_option:
                case 1:
                    manage_customer(stored_username)
                case 2:
                    print("\n" + "═" * 50)
                    manager_panel(stored_username)

        except ValueError:
            print("\n" + "-" * 50)
            print("Invalid input. Please enter a number.".center(50))
            print("-" * 50)


    except FileNotFoundError:
        print("\n" + "-" * 50)
        print("Error: User file not found.".center(50))
        print("-" * 50)