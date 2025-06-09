import  os
FILE_NAME = 'data/users.txt'

def customer_interface(username):
    print("\n" + "═" * 50)
    print("Restaurant Management System!")
    print("═" * 50)
    print(f"{username.capitalize()}, Welcome to our Restaurant ")
    print("If you want to update your profile: ")
    update_user_profile(username)

def update_user_profile(entered_username):
    print("\n" + "═" * 50)
    print("🛠️  USER PROFILE UPDATE".center(50))
    print("═" * 50)
    username_to_update = input(" 🔑 Enter your current username: ").strip()

    if not os.path.exists(FILE_NAME):
        print("⚠️ User file not found.")
        return

    updated_lines = []
    user_found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            username, email, password, role = line.strip().split(",")

            if entered_username == username_to_update:
                print("\n" + "─" * 50)
                print(f"User '{username}' found. You can now update the profile:")
                print("─" * 50)

                new_username = input(f"👤 New username (leave blank to keep '{username}'): ").strip() or username
                new_email = input(f"📧 New email (leave blank to keep '{email}'): ").strip() or email
                new_password = input(f"🔐 New password (leave blank to keep current): ").strip() or password
                new_role = input(f"🎭 New role (leave blank to keep '{role}'): ").strip() or role

                updated_line = f"{new_username},{new_email},{new_password},{new_role}\n"
                updated_lines.append(updated_line)
                user_found = True
            else:
                updated_lines.append(line)

    print("\n" + "═" * 50)
    if user_found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)
        print("✅ User profile updated successfully.")
    else:
        print("❌ Username are not matched.")
    print("═" * 50 + "\n")