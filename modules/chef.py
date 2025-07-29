import os

from modules.crud import update_profile

FILE_NAME = 'data/users.txt'
MENU_FILE = 'data/menu.txt'
ORDERS_FILE = 'data/orders.txt'

def update_chef_profile(username):
    update_profile(username)
    chef_menu(username)

def chef_menu(username):
    from modules.auth import auth_interface
    print("\n" + "═" * 50)
    print("Chef Menu".center(50))
    print("═" * 50)
    print("1. View Orders")
    print("2. Update Orders Status")
    print("3. Update Profile")
    print("4. Logout (Exit)")

    try:
        choose_number = int(input("Enter your choice (1-4): "))
        match choose_number:
            case 1:
                view_orders_chef(username)
            case 2:
                update_order_status(username)
            case 3:
                update_chef_profile(username)
            case 4:
                auth_interface()
            case _:
                print("\n" + "-" * 50)
                print("Please enter a number between 1 and 4.".center(50))
                print("-" * 50)
                chef_menu(username)
    except ValueError:
        print("\n" + "-" * 50)
        print("Invalid input. Please enter a number.".center(50))
        print("-" * 50)
        chef_menu(username)

def update_order_status(username):
    print("\n" + "═" * 70)
    print("UPDATE ORDER STATUS".center(70))
    print("═" * 70)

    if not os.path.exists(ORDERS_FILE):
        print("No orders found.")
        return

    with open(ORDERS_FILE, "r") as file:
        orders = file.readlines()

    updatable_orders = []
    print(f"{'S.N':<5}{'Customer':<15}{'Item':<20}{'Qty':<6}{'Cost':<10}{'Status':<10}")
    print("-" * 70)

    for i, line in enumerate(orders):
        parts = line.strip().split(",")
        if len(parts) == 6:
            user, item, qty, cost, order_status, payment_status = parts
            print(f"{i+1:<5}{user:<15}{item:<20}{qty:<6}{cost:<10}{order_status}")
            updatable_orders.append((i, parts))

    try:
        sn = int(input("\nEnter the S.N of the order to update: "))
        if sn < 1 or sn > len(updatable_orders):
            print("\n" + "-" * 70)
            print("Invalid selection.".center(70))
            print("-" * 70)
            chef_menu(username)
            return

        index, order_parts = updatable_orders[sn - 1]
        new_status = input("Enter new status (progress/complete): ").strip().lower()

        if new_status not in ["progress", "complete"]:
            print("\n" + "-" * 70)
            print("Invalid status.".center(70))
            print("-" * 70)
            return

        order_parts[4] = new_status  # Update order_status

        orders[index] = ",".join(order_parts) + "\n"

        with open(ORDERS_FILE, "w") as file:
            file.writelines(orders)

        print("\n" + "-" * 70)
        print(f"Order status updated to '{new_status}'.".center(70))
        chef_menu(username)

    except ValueError:
        print("\n" + "-" * 70)
        print("Invalid input.".center(70))
        print("-" * 70)
        chef_menu(username)

def view_orders_chef(username):
    print("\n" + "═" * 85)
    print("ORDERS PLACED BY CUSTOMERS".center(85))
    print("═" * 85)

    if not os.path.exists(ORDERS_FILE):
        print("No orders file found.")
        return

    with open(ORDERS_FILE, "r") as file:
        lines = file.readlines()

    if not lines:
        print("No orders have been placed yet.")
        return

    print(f"{'S.N.':<5}{'Customer':<15}{'Item Name':<20}{'Qty':<5}{'Price':<15}{'Status':<15}{'Payment'}")
    print("-" * 85)

    count = 1
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) != 6:
            continue

        username, item, qty, price, order_status, payment_status = parts
        print(f"{count:<5}{username:<15}{item:<20}{qty:<5}{'Rs.' + price:<15}{order_status:<15}{payment_status}")
        count += 1
    print("-" * 85)
    chef_menu(username)


def chef_interface(username):
    print("\n" + "═" * 50)
    print(f"{username.capitalize()}, Welcome to the Restaurant Management System!")
    chef_menu(username)
