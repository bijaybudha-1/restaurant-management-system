
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
    choose_number = int(input("Enter your choice: "))
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
            print("\n" + "═" * 50)
            manager_panel(username)

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
    print("Manager Main Panel".center(50))
    print("═" * 50)
    print("1. Manage Customers")
    print("2. Manage Menu")
    print("3. Update Profile")
    print("4. Logout (Exit)")
    choose_number = int(input("Choose an option: "))
    match choose_number:
        case 1:
            manage_customer(username)
        case 2:
            manage_menu(username)
        case 3:
            manager_update_profile(username)
        case 4:
            auth_interface()