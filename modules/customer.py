import  os
FILE_NAME = 'data/users.txt'

def customer_interface(username):
    print("\n" + "═" * 50)
    print("Restaurant Management System!".center(50))
    print(f"{username.capitalize()}, Welcome to our Restaurant ".upper().center(50))
    print("If you want to update your profile".center(50))
    update_user_profile(username)

def update_user_profile(username):
    print("\n" + "═" * 50)
    print("🛠️  USER PROFILE UPDATE".center(50))
    print("═" * 50)

    username_to_update = input("🔑 Enter your current username: ").strip()

    if not os.path.exists(FILE_NAME):
        print("⚠️  User file not found.")
        return

    updated_lines = []
    user_found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            username, email, password, role = line.strip().split(",")

            if username == username_to_update:
                print("\n" + "─" * 50)
                print(f"✅ User '{username}' found. Leave blank to keep current value.")
                print("─" * 50)

                new_username = input(f"👤 Enter your new username (leave blank to keep '{username}'): ").strip() or username
                new_email = input(f"📧 Enter your new email (leave blank to keep '{username}'): ").strip() or email
                new_password = input(f"🔐 Enter your new password [****]: ").strip() or password

                updated_line = f"{new_username},{new_email},{new_password},{role}\n"
                updated_lines.append(updated_line)
                user_found = True
            else:
                updated_lines.append(line)

    print("\n" + "═" * 50)
    if user_found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)
        print("✅ Profile updated successfully.")
    else:
        print("❌ Username not found.")
    print("═" * 50 + "\n")