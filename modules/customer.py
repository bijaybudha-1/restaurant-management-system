from modules.menu import view_menu, add_order, view_my_orders, delete_order, send_feedback

FILE_USER = 'data/users.txt'
FILE_MENU = 'data/menu.txt'

def customer_interface(username):
    print("\n" + "═" * 60)
    print(f"{username.capitalize()}, Welcome to our Restaurant ".upper().center(60))
    customer_menu(username)

def customer_menu(username):
    print("Customer Menu".center(60))
    print("═" * 60)
    print("1. View Menu")
    print("2. Place Order")
    print("3. View My Orders")
    print("4. Delete Order")
    print("5. Pay for Orders")
    print("6. Send Feedback")
    print("7. Logout (Exit)")

    user_selected = int(input("Enter your choice: "))
    match user_selected:
        case 1:
            view_menu(username)
        case 2:
            add_order(username)
        case 3:
            view_my_orders(username)
        case 4:
            delete_order(username)
        case 5:
            print("Pay of Orders")
        case 6:
            send_feedback(username)