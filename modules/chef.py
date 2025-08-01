import os

from modules.crud import update_profile

FILE_NAME = 'data/users.txt'
MENU_FILE = 'data/menu.txt'
ORDERS_FILE = 'data/orders.txt'
INGREDIENT_FILE = 'data/ingredients.txt'

def chef_interface(username):
    print("\n" + "═" * 50)
    print(f"{username.capitalize()}, Welcome to the Restaurant Management System!")
    chef_menu(username)

def chef_menu(username):
    from modules.auth import auth_interface
    print("\n" + "═" * 50)
    print("Chef Menu".center(50))
    print("═" * 50)
    print("1. View Orders")
    print("2. Update Orders Status")
    print("3. Ingredients Menu")
    print("4. Update Profile")
    print("5. Logout (Exit)")

    try:
        choose_number = int(input("Enter your choice (1-4): "))
        match choose_number:
            case 1:
                view_orders_chef(username)
            case 2:
                update_order_status(username)
            case 3:
                ingredient_request_menu(username)
            case 4:
                update_chef_profile(username)
            case 5:
                auth_interface(username)
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

# ============================  View Order Chef  ===============================
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

# =============================  Update Order Status  ===============================
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

# ------------------ Add Ingredient Request ------------------
def add_ingredient_request(username):
    print("\n" + "═" * 60)
    print("Add Ingredient Request".center(60))
    print("═" * 60)

    name = input("Enter ingredient name: ").strip().lower()
    quantity = input("Enter quantity: ").strip().lower()
    unit = input("Enter unit (e.g., kg, liter, packet): ").strip().lower()
    note = input("Enter note/reason (optional): ").strip().lower()

    if not name or not quantity or not unit:
        print("Ingredient name, quantity, and unit are required.")
        return

    with open(INGREDIENT_FILE, "a") as file:
        file.write(f"{username},{name},{quantity},{unit},{note}\n")

    print(f"\nRequest for '{name}' added successfully!")


# ------------------ Edit Ingredient Request ------------------
def edit_ingredient_request(username):
    view_ingredient_requests(username)
    if not os.path.exists(INGREDIENT_FILE):
        return

    try:
        req_num = int(input("Enter the request number to edit: ").lower())
        with open(INGREDIENT_FILE, "r") as file:
            lines = file.readlines()

        count = 0
        updated_lines = []

        for line in lines:
            user, name, qty, unit, note = line.strip().split(",")
            if user == username:
                count += 1
                if count == req_num:
                    print(f"Editing Request: {name}")
                    new_qty = input(f"Enter new quantity (current: {qty}): ").strip().lower() or qty
                    new_unit = input(f"Enter new unit (current: {unit}): ").strip().lower() or unit
                    new_note = input(f"Enter new note (current: {note}): ").strip().lower() or note
                    updated_lines.append(f"{user},{name},{new_qty},{new_unit},{new_note}\n")
                    continue
            updated_lines.append(line)

        with open(INGREDIENT_FILE, "w") as file:
            file.writelines(updated_lines)

        print("\n" + "-" * 70)
        print("Ingredient request updated successfully.")
        print("-" * 70)

    except ValueError:
        print("\n" + "-" * 70)
        print("Invalid input.")
        print("-" * 70)

# ------------------ Delete Ingredient Request ------------------
def delete_ingredient_request(username):
    view_ingredient_requests(username)

    if not os.path.exists(INGREDIENT_FILE):
        return

    try:
        req_num = int(input("Enter the request number to delete: ").lower())
        with open(INGREDIENT_FILE, "r") as file:
            lines = file.readlines()

        count = 0
        updated_lines = []
        deleted = False

        for line in lines:
            user, name, qty, unit, note = line.strip().split(",")
            if user == username:
                count += 1
                if count == req_num:
                    deleted = True
                    print("\n" + "-" * 70)
                    print(f"Deleted request for: {name}")
                    print("-" * 70)
                    continue
            updated_lines.append(line)

        with open(INGREDIENT_FILE, "w") as file:
            file.writelines(updated_lines)

        if not deleted:
            print("\n" + "-" * 70)
            print("Request not found.")
            print("-" * 70)
    except ValueError:
        print("\n" + "-" * 70)
        print("Invalid input.")
        print("-" * 70)

# ------------------ View Ingredient Requests ------------------
def view_ingredient_requests(username):
    print("\n" + "═" * 70)
    print("Your Ingredient Requests".center(70))
    print("═" * 70)

    if not os.path.exists(INGREDIENT_FILE):
        print("\n" + "-" * 70)
        print("No requests found.")
        print("-" * 70)
        return

    found = False
    with open(INGREDIENT_FILE, "r") as file:
        print("-" * 70)
        print(f"{'S.N':<5}{'Item Name':<20}{'Qty':<5}{"unit":<5}{'note/reasons':}")
        print("-" * 70)
        for i, line in enumerate(file, start=1):
            user, name, qty, unit, note = line.strip().split(",")
            if user == username:
                print(f"{i:<5}{name.title():<15}{qty.title():<20}{unit.title():<5}{note.title()}")
                found = True
        print("\n" + "-" * 70)

    if not found:
        print("\n" + "-" * 70)
        print("You have no ingredient requests.")
        print("-" * 70)

# ------------------ Ingredient Request Menu ------------------
def ingredient_request_menu(username):
    while True:
        print("\n" + "═" * 60)
        print(f"Chef Menu - Ingredient Request".center(60))
        print("═" * 60)
        print("1. Add Ingredient Request")
        print("2. Edit Request")
        print("3. Delete Request")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    add_ingredient_request(username)
                case 2:
                    edit_ingredient_request(username)
                case 3:
                    delete_ingredient_request(username)
                case 4:
                    chef_menu(username)
                    break
                case _:
                    print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")


# ==============================  Update Own Profile  ==================================
def update_chef_profile(username):
    update_profile(username)
    chef_menu(username)

