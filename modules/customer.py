
from modules.crud import update_profile
from modules.menu import view_menu, add_order, view_my_orders, delete_order, send_feedback, pay_order

FILE_USER = 'data/users.txt'
FILE_MENU = 'data/menu.txt'

def customer_interface(username):
    print("\n" + "═" * 60)
    print(f"{username.capitalize()}, Welcome to our Restaurant ".upper().center(60))
    customer_menu(username)

def update_own_profile(username):
    update_profile(username)
    customer_menu(username)

def customer_menu(username):
    from modules.auth import auth_interface
    print("Customer Menu".center(60))
    print("═" * 60)
    print("1. View Menu")
    print("2. Place Order")
    print("3. View My Orders")
    print("4. Delete Order")
    print("5. Pay for Orders")
    print("6. Send Feedback")
    print("7. Update Profile")
    print("8. Logout (Exit)")

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
            pay_order(username)
        case 6:
            send_feedback(username)
        case 7:
            update_own_profile(username)
        case 8:
            auth_interface()