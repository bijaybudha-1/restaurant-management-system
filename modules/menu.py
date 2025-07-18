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
