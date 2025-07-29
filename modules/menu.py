import os

MENU_FILE = 'data/menu.txt'
ORDERS_FILE = 'data/orders.txt'
FEEDBACK_FILE = 'data/feedback.txt'

# Customer Menu Crud Operation
def view_menu(username):
    from modules.customer import customer_menu
    print("\n" + "═" * 60)
    print("View Menu".upper().center(60))
    print("═" * 60)
    food_id = 1
    file = open(MENU_FILE, 'r')
    print(f"{'S.N':<5}{'Name':<20}{'Category':<15}{'Unit':<10}{'Price'}")
    print("-" * 60)
    for line in file:
        name, category, unit, price = line.strip().split(",")
        print(f"{food_id:<5}{name:<20}{category:<15}{unit:<10}{price}")
        food_id += 1
    print("\n" + "═" * 60)
    user_choose = input("If you would like to place order, enter Y or N: ")
    match user_choose.lower():
        case "y":
            add_order(username)
        case "n":
            print("\n" + "═" * 60)
            customer_menu(username)
    print("\n" + "═" * 60)
    customer_menu(username)

def add_order(username):
    from modules.customer import customer_menu

    print("\n" + "═" * 60)
    print("Place Order".center(60))
    print("═" * 60)

    # temporary list to store ordered items
    order_items = []
    order_items_num = 1

    while True:
        item_name = input("Enter item name: ").strip()
        quantity_input = input("Enter quantity: ").strip()

        if not item_name or not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("\n" + "-" * 60)
            print("Invalid input.".center(60))
            print("-" * 60)
        else:
            quantity = int(quantity_input)
            found = False
            try:
                with open("data/menu.txt", "r") as menu_file:
                    for line in menu_file:
                        name, category, unit, price = line.strip().split(",")
                        if name.lower() == item_name.lower():
                            total = float(price) * quantity
                            order_items.append((name, quantity, total))
                            print("\n" + "-" * 60)
                            print(f"Added: {quantity} x {name} = Rs.{total:.2f}")
                            print("-" * 60)
                            found = True
                            break
                if not found:
                    print("\n" + "-" * 60)
                    print("Item not found.".center(60))
                    print("-" * 60)
            except FileNotFoundError:
                print("\n" + "-" * 60)
                print("Menu file not found.".center(60))
                print("-" * 60)
                customer_menu(username)
                return

        # Ask if they want to add more items
        choice = input("Do you want to order another item? (y/n): ").strip().lower()
        if choice != 'y':
            break

    if not order_items:
        print("\n" + "-" * 60)
        print("No items in order.".center(60))
        print("-" * 60)
        print("\n" + "═" * 60)
        customer_menu(username)
        return

    # Show order summary
    print("\n" + "═" * 60)
    print("Order Summary".center(60))
    print("═" * 60)
    grand_total = 0
    print(f"{'S.N':<5}{'Item Name':<25}{'Quantity':<15}{'Price'}")
    print("-" * 60)
    for name, qty, total in order_items:
        print(f"{order_items_num:<5}{name:<25} {qty:<15}Rs.{total:.2f}")
        grand_total += total
        order_items_num += 1
    print("\n" + "-" * 60)
    print(f"{'Total':>45} : Rs.{grand_total:.2f}")
    print("-" * 60)

    confirm = input("Do you want to confirm this order? (y/n): ").strip().lower()
    if confirm == 'y':
        with open("data/orders.txt", "a") as order_file:
            for name, qty, total in order_items:
                order_file.write(f"{username},{name},{qty},{total:.2f},pending,unpaid\n")
        print("\n" + "-" * 60)
        print("Order confirmed and saved!".center(60))
        print("-" * 60)
        user_choose = input("If you would like to View your order, enter Y or N: ")
        match user_choose.lower():
            case "y":
                view_my_orders(username)
            case "n":
                return

    else:
        print("\n" + "-" * 60)
        print("Order canceled.".center(60))
        print("-" * 60)
    print("\n" + "═" * 60)
    customer_menu(username)


# View my Order Function

def view_my_orders(username):
    from modules.customer import customer_menu
    from modules.customer import add_order
    print("\n" + "═" * 80)
    print("MY ORDERS".center(80))
    print("═" * 80)

    if not os.path.exists(ORDERS_FILE):
        print("No orders found.")
        print("═" * 80)
        return

    with open(ORDERS_FILE, "r") as file:
        lines = file.readlines()

    total = 0
    has_orders = False
    print(f"{'S.N.':<5}{'Item Name':<20}{'Qty':<5}{'Price':<15}{'Order Status':<15}{'Payment Status'}")
    print("-" * 80)

    count = 1
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) != 6:
            continue  # Skip invalid lines

        user, name, qty, cost, order_status, payment_status = parts
        if user == username:
            print(f"{count:<5}{name:<20}{qty:<5}{'Rs.' + cost:<15}{order_status:<15}{payment_status}")
            total += float(cost)
            count += 1
            has_orders = True

    if has_orders:
        print("-" * 80)
        print(f"{'Total Amount':>65} : Rs.{total:.2f}")
    else:
        print("No orders found.".center(80))
    print("-" * 80)

    user_choose = input("Would you like to place a new order? (Y/N): ").strip().lower()
    if user_choose == 'y':
        add_order(username)
    else:
        print("\n" + "═" * 80)
        customer_menu(username)


# Allow the user to delete one of their pending orders.
# Delete Order
def delete_order(username):
    from modules.customer import customer_menu
    if not os.path.exists(ORDERS_FILE):
        print("\n" + "-" * 60)
        print("No orders to delete.".center(60))
        print("-" * 60)
        return

    with open(ORDERS_FILE, "r") as file:
        lines = file.readlines()

    new_lines = []
    deleted = False
    item_to_delete = input("Enter the name of the item you want to delete from your order: ").strip().lower()

    for line in lines:
        fields = line.strip().split(",")
        if len(fields) >= 5:
            user, name = fields[0], fields[1]
            status = fields[4].lower()
            if user == username and name.lower() == item_to_delete and status == "pending":
                deleted = True
                continue  # skip this line (delete it)
        new_lines.append(line)

    with open(ORDERS_FILE, "w") as file:
        file.writelines(new_lines)

    if deleted:
        print("\n" + "-" * 60)
        print(f"Order for '{item_to_delete}' deleted.".center(60))
        print("-" * 60)
        print("\n" + "═" * 60)
        customer_menu(username)
    else:
        print("\n" + "-" * 60)
        print(f"No pending order found for '{item_to_delete}'.".center(60))
        print("-" * 60)
        print("\n" + "═" * 60)
        customer_menu(username)

# Send feedback
def send_feedback(username):
    from modules.customer import customer_menu

    print("\n" + "═" * 60)
    print("SEND FEEDBACK".center(60))
    print("═" * 60)

    feedback = input("Enter your feedback: ").strip()

    if not feedback:
        print("\n" + "-" * 60)
        print("Feedback cannot be empty.".center(60))
        print("-" * 60)
        print("\n" + "═" * 60)
        customer_menu(username)
        return

    try:
        with open(FEEDBACK_FILE, "a") as file:
            file.write(f"{username},{feedback}\n")
        print("\n" + "-" * 60)
        print("Your feedback has been sent to the administrator.".center(60))
        print("-" * 60)
    except Exception as e:
        print("Failed to send feedback:", str(e))

    print("\n" + "═" * 60)
    customer_menu(username)


def pay_order(username):
    from modules.customer import customer_menu
    print("\n" + "═" * 60)
    print("CHECK & PAY YOUR ORDERS".center(60))
    print("═" * 60)

    if not os.path.exists(ORDERS_FILE):
        print("No orders found.")
        print("═" * 60)
        return

    with open(ORDERS_FILE, "r") as file:
        lines = file.readlines()

    unpaid_orders = []
    updated_lines = []
    total_to_pay = 0
    has_unpaid = False

    for line in lines:
        parts = line.strip().split(",")
        if len(parts) != 6:
            updated_lines.append(line)
            continue

        user, name, qty, cost, order_status, payment_status = parts

        if user == username and order_status.lower() == "complete" and payment_status.lower() == "unpaid":
            unpaid_orders.append((name, qty, cost))
            total_to_pay += float(cost)
            updated_lines.append(f"{user},{name},{qty},{cost},{order_status},Paid\n")
            has_unpaid = True
        else:
            updated_lines.append(line)

    if has_unpaid:
        print("-" * 60)
        print(f"{'S.N':<5}{'Item Name':<20}{'Qty':<10}{'Price (Rs.)'}")
        print("-" * 60)
        for i, (name, qty, cost) in enumerate(unpaid_orders, start=1):
            print(f"{i:<5}{name:<20}{qty:<10}{cost}")
        print("-" * 60)
        print(f"{'Total to Pay':>40} : Rs.{total_to_pay:.2f}")
        print("-" * 60)

        confirm = input("Do you want to proceed with payment? (Y/N): ").strip().lower()
        print("\n" + "-" * 60)
        if confirm == 'y':
            with open(ORDERS_FILE, "w") as file:
                file.writelines(updated_lines)
            print(f"Payment successful! Total paid: Rs.{total_to_pay:.2f}".center(60))
            print("-" * 60)
        else:
            print("Payment cancelled.".center(60))
            print("-" * 60)
    else:
        print("\n" + "-" * 60)
        print("No unpaid and completed orders found.".center(60))
        print("-" * 60)

    print("\n" + "═" * 60)
    customer_menu(username)


def view_order_status():
    print("View Order Status")

# Manager Manage Menu Panel
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