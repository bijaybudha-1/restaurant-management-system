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

def manage_menu(username):
    from modules.manager import manager_panel
    print("\n" + "═" * 60)
    print("Manage Menu".center(60))
    print("═" * 60)
    print("1. Add Food")
    print("2. View Food")
    print("3. Update Food")
    print("4. Delete Food")
    print("5. Back to Manager Main Panel")
    choose_number = int(input("Choose an option: "))
    match choose_number:
        case 1:
            add_item()
        case 2:
            view_all_items()
        case 3:
            update_item()
        case 4:
            delete_item()
        case 5:
            print("\n" + "═" * 50)
            manager_panel(username)

# Add New Food Item
def add_item():
    print("\n" + "═" * 60)
    print("Add New Food".center(60))
    print("═" * 60)

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
                    print("\n" + "-" * 60)
                    print(f"'{item_name}' is already added.")
                    print("-" * 60)
                    manage_menu(None)
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
                print("\n" + "-" * 60)
                print("Price must be a positive number.".center(60))
                print("-" * 60)
            else:
                break
        except ValueError:
            print("\n" + "-" * 60)
            print("Invalid price format. Please enter a valid number.".center(60))
            print("-" * 60)

    # Save the new item to the file
    with open(MENU_FILE, "a") as file:
        file.write(f"{item_name},{category},{unit},{price:.2f}\n")

    print("\n" + "-" * 60)
    print("Added new food successfully.".center(60))
    print("-" * 60)
    manage_menu(None)

# View All Items
def view_all_items():
    print("\n" + "═" * 60)
    print("View All Food Items".center(60))
    print("═" * 60)

    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No food items found.")
                manage_menu(None)
                return
            else:
                print(f"{'Item Name':<20} {'Category':<15} {'Unit':<10} {'Price':<10}")
                print("-" * 60)
                for line in lines:
                    item_name, category, unit, price = line.strip().split(",")
                    print(f"{item_name:<20} {category:<15} {unit:<10} {price:<10}")
    else:
        print("Menu file does not exist.")
    manage_menu(None)

# Update Item function
def update_item():
    print("\n" + "═" * 60)
    print("Update Food Item".center(60))
    print("═" * 60)

    search_name = input("Enter the item name to update: ").strip().lower()

    if not os.path.exists(MENU_FILE):
        print("\n" + "-" * 60)
        print("Menu file not found.")
        print("-" * 60)
        manage_menu(None)
        return

    with open(MENU_FILE, "r") as file:
        lines = file.readlines()

    updated = False
    for i in range(len(lines)):
        item = lines[i].strip().split(",")
        if item[0].lower() == search_name:
            print(f"Found item name: {item[0].strip().title()}")

            new_name = input("Enter new name: ").strip().lower()
            new_category = input("Enter new category: ").strip().lower()
            new_unit = input("Enter new unit: ").strip().lower()
            new_price = input("Enter new price: ").strip().lower()

            # Replace old line with new values
            lines[i] = f"{new_name},{new_category},{new_unit},{new_price}\n"
            updated = True
            break

    if updated:
        with open(MENU_FILE, "w") as file:
            file.writelines(lines)
        print("\n" + "-" * 60)
        print("Item updated successfully.".center(60))
        print("-" * 60)
    else:
        print("\n" + "-" * 60)
        print("Item not found.".center(60))
        print("-" * 60)
    manage_menu(None)

# Delete Item
def delete_item():
    print("\n" + "═" * 60)
    print("Delete Food Item".center(60))
    print("═" * 60)

    item_to_delete = input("Enter the item name you want to delete: ").strip().lower()

    if not os.path.exists(MENU_FILE):
        print("\n" + "-" * 60)
        print("Menu file not found.".center(60))
        print("-" * 60)
        manage_menu(None)
        return

    with open(MENU_FILE, "r") as file:
        lines = file.readlines()

    found = False
    updated_lines = []
    for line in lines:
        item_name = line.strip().split(",")[0].lower()
        if item_name == item_to_delete:
            found = True
            continue
        updated_lines.append(line)

    if found:
        with open(MENU_FILE, "w") as file:
            file.writelines(updated_lines)
        print("\n" + "-" * 60)
        print(f"'{item_to_delete.capitalize()}' has been deleted from the menu.".center(60))
        print("-" * 60)
    else:
        print("\n" + "-" * 60)
        print(f"Item '{item_to_delete.capitalize()}' not found.".center(60))
        print("-" * 60)
    manage_menu(None)