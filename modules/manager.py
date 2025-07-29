
from modules.crud import update_profile, add_customer, update_customer_profile, delete_customer, view_customer
from modules.menu import manage_menu


def manage_customer(username):
    print("\n" + "═" * 50)
    print("Manage Customer Panel".center(50))
    print("═" * 50)
    print("1. Add Customer")
    print("2. View Customer")
    print("3. Update Customer")
    print("4. Delete Customer")
    print("5. Back to Manager Main Panel")

    try:
        choose_number = int(input("Enter your choice (1-5): "))
        match choose_number:
            case 1:
                add_customer(username)
            case 2:
                view_customer(username)
            case 3:
                update_customer_profile(username)
            case 4:
                delete_customer(username)
            case 5:
                manager_panel(username)
            case _:
                print("\n" + "-" * 50)
                print("Please enter a number between 1 and 5.".center(50))
                print("-" * 50)
                manage_customer(username)
    except ValueError:
        print("\n" + "-" * 50)
        print("Invalid input. Please enter a number.".center(50))
        print("-" * 50)
        manage_customer(username)
def manager_update_profile(username):
    update_profile(username)
    print("═" * 50)
    manager_panel(username)

def manager_interface(username):
    print("\n" + "═" * 50)
    print(f"{username}, Welcome to the Restaurant Management System!")
    manager_panel(username)

def manager_panel(username):
    from modules.auth import auth_interface
    print("\n" + "═" * 50)
    print("Manager Main Panel".center(50))
    print("═" * 50)
    print("1. Manage Customers")
    print("2. Manage Menu")
    print("3. Update Profile")
    print("4. Logout (Exit)")

    try:
        choose_number = int(input("Choose an option (1–4): "))
        match choose_number:
            case 1:
                manage_customer(username)
            case 2:
                manage_menu(username)
            case 3:
                manager_update_profile(username)
            case 4:
                auth_interface()
            case _:
                print("\n" + "-" * 50)
                print("Please enter a number between 1 and 4.".center(50))
                print("-" * 50)
                manager_panel(username)
    except ValueError:
        print("\n" + "-" * 50)
        print("Invalid input. Please enter a number.".center(50))
        print("-" * 50)
        manager_panel(username)
