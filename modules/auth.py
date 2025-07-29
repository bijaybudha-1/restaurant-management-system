import os
from random import randint

from modules.admin import greeting_interface
from modules.customer import customer_interface
from modules.chef import chef_interface
from modules.manager import manager_interface

USER_FILE = 'data/users.txt'

# ======================================  Auth Interface  ==================================
def auth_interface():
    print("═" * 50)
    print("Welcome to Restaurant Management System!".center(50))
    print("User Authentication Interface".center(50))
    print("═" * 50)
    print("1. Register a new user")
    print("2. User Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            registration()
        case "2":
                login()
        case "3":
                exit()

# ============================  Registration  ==============================
def registration():
    print("═" * 50)
    print("User Registration".center(50).upper())
    print("═" * 50)
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user_role = "customer"

    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                if line.strip().split(",")[0] == username:
                    print(f"{username} is already registered.")
                    return
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{email},{password},{user_role}\n")
    print("Registration successful.")
    login()

# =============================  login  ===================================
def login():
    print("\n" + "═" * 50)
    print("User Login".center(50).upper())
    print("═" * 50)
    username_email = input("Enter your username or email: ")
    password = input("Enter your password: ")
    user_role = input("Enter your role: ")
    message = "Login successful."
    attempt = 3
    if not os.path.exists(USER_FILE):
        print("User doesn't exist.")
        return

    with open(USER_FILE, "r") as file:
        for each_file_line in file:
            stored_username, stored_email, stored_password, stored_user_role = each_file_line.strip().split(",")
            if username_email ==  stored_email or username_email == stored_username:
                while attempt > 0:
                    if password == stored_password:
                        if stored_user_role == user_role == "admin":
                            print("\n" + "-" * 50)
                            print(f"{message}".center(50).upper())
                            print("-" * 50)
                            greeting_interface(stored_username)
                            return
                        elif stored_user_role == user_role == "manager":
                            print("\n" + "-" * 50)
                            print(f"{message}".center(50).upper())
                            print("-" * 50)
                            manager_interface(stored_username)
                            return
                        elif stored_user_role == user_role == "chef":
                            print("\n" + "-" * 50)
                            print(f"{message}".center(50).upper())
                            print("-" * 50)
                            chef_interface(stored_username)
                            return
                        elif stored_user_role == user_role == "customer":
                            print("\n" + "-" * 50)
                            print(f"{message}".center(50).upper())
                            print("-" * 50)
                            customer_interface(stored_username)
                            return
                        else:
                            print("\n" + "-" * 50)
                            print("Invalid role.".center(50).upper())
                            print("-" * 50)
                            return
                    else:
                        attempt -= 1
                        if attempt > 0:
                            print(f"Incorrect password. Attempts left: {attempt}")
                            password = input("Enter your password: ")
                        else:
                            print("Invalid password.")
                            reset_password(stored_email)
                return

    print("\n" + "-" * 50)
    print("Username or email not found.")
    print("-" * 50)

#  =================================  Reset Password  ====================================
def reset_password(stored_email):
    reset_status = input("Do you want to reset your password? (y/n): ")
    if reset_status.lower() ==  "y":
        email_checker(stored_email)
    elif reset_status.lower() == "n":
        auth_interface()
    else:
        print("Invalid input key.")

# =========================  Email Check  ================================
def email_checker(stored_email):
    print("\n" + "═" * 50)
    print("Email Verification".center(50).upper())
    print("═" * 50)
    email = input("Enter your email: ")
    attempt = 3
    while attempt > 0:
        if email == stored_email:
            otp_generator(email)
            return
        else:
            attempt -= 1
            if attempt > 0:
                print(f"Incorrect email. Attempts left: {attempt}")
                email = input("Enter your email: ")
            else:
                print("─" * 50)
                print("You have entered wrong email 3 times. Access denied.")
                print("─" * 50)

# ===========================  OTP Generator  ===============================
def otp_generator(email):
    print("\n" + "═" * 50)
    print("OTP Code Generator".center(50).upper())
    print("═" * 50)
    otp = randint(1000, 9999)
    print(f"This is your OTP code: {otp}")
    entered_otp = input("Enter your OTP code: ")
    otp_checker(otp, entered_otp, email)

# ===============================  OTP Checker  ==================================
def otp_checker(otp, entered_otp, email):
    print("\n" + "═" * 50)
    print(f"OTP Checker".center(50))
    print("═" * 50)
    if str(otp) == entered_otp:
        print(f"Your OTP code is correct.".center(50))
        password_reset(email)
    else:
        print(f"Your OTP code is incorrect.")
        print("─" * 50)

# =================================  Password Reset  ===================================
def password_reset(email):
    print("\n" + "═" * 50)
    print("RESET YOUR PASSWORD".center(50))
    print("═" * 50)

    new_password = input("Enter your new password: ").strip()
    confirm_password = input("Confirm your new password: ").strip()

    if new_password != confirm_password:
        print("Passwords do not match. Please try again.")
        return

    if not os.path.exists(USER_FILE):
        print("User file not found.")
        return

    updated_lines = []
    user_found = False

    with open(USER_FILE, "r") as file:
        for line in file:
            stored_username, stored_email, password, stored_role = line.strip().split(",")

            if stored_email == email:
                updated_line = f"{stored_username},{stored_email},{new_password},{stored_role}\n"
                user_found = True
            else:
                updated_line = line

            updated_lines.append(updated_line)

    print("\n" + "═" * 50)
    if user_found:
        with open(USER_FILE, "w") as file:
            file.writelines(updated_lines)
        print("Password updated successfully.")
    else:
        print("Username not found.")
    print("═" * 50 + "\n")
