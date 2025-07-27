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
    choose_item = int(input("Enter food item number: "))

def pay_order():
    print("\n" + "═" * 50)
    print("Pay Order")
    print("═" * 50)

def view_order_status():
    print("View Order Status")

def menu_interface():
    print("\n" + "═" * 50)
    print("Customer Menu".center(50))
    print("═" * 50)

# Add New Food Item
def add_item():
    from modules.manager import manage_menu

    print("\n" + "═" * 50)
    print("Add New Food".center(50))
    print("═" * 50)

    # Input Item name
    while True:
        item_name = input("Enter a item name: ").strip().lower()
        if not item_name:
            print("Field is empty. Please enter a item name.")
        else:
            break

    # Input Item Category
    while True:
        category = input("Enter a item category(e.g.,\nVeg, Non-Veg, Dessert, Beverages): ").strip().lower()
        if not category:
            print("Field is empty. Please enter a item category.")
        else:
            break

    # Item Unit (plate, pieces, glass, )
    while True:
        unit = input("Enter a item unit (e.g.,\nplate, pcs, glass): ").strip().lower()
        if not unit:
            print("Field is empty. Please enter a item unit.")
        else:
            break

    # Input Item Price
    item_price = input("Enter a item price: ").strip()
    try:
        price = float(item_price)
        if price <= 0:
            print("Price must be a positive number.")
            return
    except ValueError:
        print("Invalid price format. Use numbers like 12.50.")
        return


    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, "r") as file:
            for line in file:
                if line.strip().split(",")[0] == item_name:
                    print(f"{item_name} is already Added.")
                    return

    with open(MENU_FILE, "a") as file:
        file.write(f"{item_name},{category},{unit},{price}\n")
    print("\n" + "═" * 50)
    print("Added new food successfully.".center(50))
    print("═" * 50)
    manage_menu()