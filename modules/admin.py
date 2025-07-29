import os
from datetime import datetime

from modules.crud import admin_add_user, view_staff, update_profile, update_user_profile, delete_user_profile
from modules.menu import ORDERS_FILE

USER_FILE = 'data/users.txt'
FEEDBACK_FILE = 'data/feedback.txt'

def manage_staff(username):
    while True:
        print("\n" + "═" * 50)
        print("Manage Staff Interface".center(50))
        print("═" * 50)
        print("1. Add New Staff")
        print("2. View All Staff")
        print("3. Update Staff Profile")
        print("4. Delete Staff Profile")
        print("5. Back to Admin Panel")

        try:
            admin_choose = int(input("Choose an option (1–5): ").strip())
            match admin_choose:
                case 1:
                    admin_add_user(username)
                    break
                case 2:
                    view_staff(username)
                    break
                case 3:
                    update_user_profile(username)
                    break
                case 4:
                    delete_user_profile()
                    break
                case 5:
                    print("\n" + "═" * 50)
                    admin_interface(username)
                    break
                case _:
                    print("\n" + "-" * 50)
                    print("Please enter a number between 1 and 5.".center(50))
                    print("-" * 50)
        except ValueError:
            print("\n" + "-" * 50)
            print("Invalid input. Please enter a valid number.".center(50))
            print("-" * 50)


def view_sales_report(username):
    print("\n" + "═" * 50)
    print("SALES REPORT PANEL".center(50))
    print("═" * 50)

    if not os.path.exists(ORDERS_FILE):
        print("\n" + "-" * 50)
        print("No order data found.")
        print("-" * 50)
        return

    with open(ORDERS_FILE, "r") as file:
        lines = file.readlines()

    # Only process valid completed & paid orders
    valid_orders = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 6:
            user, item, qty, price, order_status, payment_status = parts
            if order_status.lower() == "complete" and payment_status.lower() == "paid":
                valid_orders.append({
                    "user": user,
                    "item": item,
                    "qty": int(qty),
                    "price": float(price)
                })

    if not valid_orders:
        print("\n" + "-" * 50)
        print("No completed and paid orders available.")
        print("-" * 50)
        admin_interface(username)
        return

    # Menu to choose report type
    print("1. Total Sales")
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("/n" + "-" * 50)
        print("Invalid input.".center(50))
        print("-" * 50)
        admin_interface(username)
        return
    print("\n" + "-" * 50)

    if choice == 1:
        total_sales = sum(order["price"] for order in valid_orders)
        print(f"TOTAL SALES AMOUNT: Rs.{total_sales:.2f}")
        print("-" * 50)
        admin_interface(username)
    else:
        print("Invalid option selected.".center(50))
        print("-" * 50)
        admin_interface(username)

    print("-" * 50)


def view_feedback(stored_username):
    print("\n" + "═" * 50)
    print("CUSTOMER FEEDBACK".center(50))
    print("═" * 50)

    if not os.path.exists(FEEDBACK_FILE) or os.path.getsize(FEEDBACK_FILE) == 0:
        print("No feedback received yet.".center(50))
        print("═" * 50)
        return

    with open(FEEDBACK_FILE, "r") as file:
        lines = file.readlines()

    print(f"{'S.N.':<6}{'Username':<20}{'Feedback'}")
    print("-" * 50)

    for i, line in enumerate(lines, start=1):
        parts = line.strip().split(",", 1)
        if len(parts) == 2:
            username, feedback = parts
            print(f"{i:<6}{username:<20}{feedback}")
        else:
            print(f"{i:<6}{'Invalid Entry':<20}{line.strip()}")

    print("\n" + "═" * 50)
    admin_interface(stored_username)

def greeting_interface(username):
    print("\n" + "═" * 50)
    print(f"{username.upper()}, Welcome to the Restaurant Management System ".center(50))
    admin_interface(username)


def update_own_profile(username):
    update_profile(username)
    admin_interface(username)

def admin_interface(username):
    from modules.auth import auth_interface
    while True:
        print("\n" + "═" * 50)
        print("Admin Panel".center(50))
        print("═" * 50)
        print("1. Manage Staff")
        print("2. View Sales Report")
        print("3. View Feedback")
        print("4. Update Profile")
        print("5. Log out (Exit)")
        print("═" * 50)

        try:
            admin_choose = int(input("Choose an option (1–5): ").strip())
            match admin_choose:
                case 1:
                    manage_staff(username)
                    break
                case 2:
                    view_sales_report(username)
                    break
                case 3:
                    view_feedback(username)
                    break
                case 4:
                    update_own_profile(username)
                    break
                case 5:
                    auth_interface()
                    break
                case _:
                    print("-" * 50)
                    print("Please select a number between 1 and 5.".center(50))
                    print("-" * 50)
        except ValueError:
            print("\n" + "-" * 50)
            print("Invalid input. Please enter a number.".center(50))
            print("-" * 50)