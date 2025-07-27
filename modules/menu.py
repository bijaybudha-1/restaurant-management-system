import os
MENU_FILE = 'data/menu.txt'

def view_order_menu():
    print("\n" + "═" * 50)
    print("View Menu".upper().center(50))
    print("═" * 50)
    food_id = 1
    file = open(MENU_FILE, 'r')
    for line in file:
        stored_name, stored_price = line.strip().split(",")
        print(f"{food_id}. Food Name: {stored_name}: Price: {stored_price}")
        food_id += 1
    print("\n" + "═" * 50)
    user_choose = input("If you would like to place order, enter Y or N: ")
    match user_choose.lower():
        case "y":
            place_order()
        case "n":
            exit()

def place_order():
    print("Place Order Interface".center(50))
    print("═" * 50)
    # choose_item = int(input("Enter food item number: "))

def pay_order():
    print("\n" + "═" * 50)
    print("Pay Order")
    print("═" * 50)

def view_order_status():
    print("View Order Status")

def manage_menu():
    print("\n" + "═" * 50)
    print("Manage Menu".center(50))
    print("═" * 50)
    print("1. Add Food")
    print("2. View Food")
    print("3. Update Food")
    print("4. Delete Food")
    choose_number = int(input("Choose an option: "))
    match choose_number:
        case 1:
            add_item()
        case 2:
            print("view item")
        case 3:
            print("Update Food")
        case 4:
            print("Delete Food")
        case 5:
            print("Back to Menu")

# Add New Food Item
def add_item():
    print("\n" + "═" * 50)
    print("Add New Food".center(50))
    print("═" * 50)

    # Input Item name
    while True:
        item_name = input("Enter item name: ").strip().lower()
        if not item_name:
            print("Field is empty. Please enter an item name.")
        else:
            break

    # Check if item already exists
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, "r") as file:
            for line in file:
                if line.strip().split(",")[0] == item_name:
                    print(f"'{item_name}' is already added.")
                    manage_menu()
                    return

    # Input Item Category
    while True:
        category = input("Enter item category (e.g., Veg, Non-Veg, Dessert, Beverages): ").strip().lower()
        if not category:
            print("Field is empty. Please enter an item category.")
        else:
            break

    # Item Unit (plate, pieces, glass)
    while True:
        unit = input("Enter item unit (e.g., plate, pcs, glass): ").strip().lower()
        if not unit:
            print("Field is empty. Please enter an item unit.")
        else:
            break

    price = 0
    # Input Item Price with proper validation
    while True:
        price_input = input("Enter price (e.g., 12.50): ").strip()

        if not price_input:
            print("Field is empty. Please enter a price.")
            continue

        try:
            price = float(price_input)
            if price <= 0:
                print("Price must be a positive number.")
            else:
                break
        except ValueError:
            print("Invalid price format. Please enter a valid number.")

    # Save the new item to the file
    with open(MENU_FILE, "a") as file:
        file.write(f"{item_name},{category},{unit},{price:.2f}\n")

    print("\n" + "═" * 50)
    print("Added new food successfully.".center(50))
    print("═" * 50)

    manage_menu()