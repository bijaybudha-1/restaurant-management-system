import os
from unittest import case

from modules.admin import admin_interface
from modules.customer import customer_interface
from modules.chef import chef_interface
from modules.manager import manager_interface

FILE_NAME = 'data/users.txt'

def registration():
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user_role = "customer"

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.strip().split(",")[0] == username:
                    print(f"{username} is already registered.")
                    return
    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{email},{password},{user_role}\n")
    print("Registration successful.")
    login()


def login():
    username_email = input("Enter your username or email: ")
    password = input("Enter your password: ")
    user_role = input("Enter your role: ")
    message = "Login successful."
    attempt = 3
    if not os.path.exists(FILE_NAME):
        print("User doesn't exist.")
        return

    with open(FILE_NAME, "r") as file:
        for each_file_line in file:
            stored_username, stored_email, stored_password, stored_user_role = each_file_line.strip().split(",")
            if username_email ==  stored_email or username_email == stored_username:
                while attempt > 0:
                    if password == stored_password:
                        if stored_user_role == user_role == "admin":
                            print(f"{message}")
                            admin_interface(stored_username)
                            return
                        elif stored_user_role == user_role == "manager":
                            print(f"{message}")
                            manager_interface(stored_username)
                            return
                        elif stored_user_role == user_role == "chef":
                            print(f"{message}")
                            chef_interface(stored_username)
                            return
                        elif stored_user_role == user_role == "customer":
                            print(f"{message}")
                            customer_interface(stored_username)
                            return
                        else:
                            print("Invalid role.")
                            return
                    else:
                        attempt -= 1
                        if attempt > 0:
                            print(f"Incorrect password. Attempts left: {attempt}")
                            password = input("Enter your password: ")
                        else:
                            print("Login failed. No more attempts.")
                            return
                return

    print("Username or email not found.")


def auth_interface():
    print("Welcome to Restaurant Management System!")
    print("User registration form")
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

