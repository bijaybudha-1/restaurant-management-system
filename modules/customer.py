from modules.menu import view_menu

FILE_USER = 'data/users.txt'
FILE_MENU = 'data/menu.txt'


def send_feedback():
    print("\n" + "═" * 50)
    print("Please drop your feedback below.".upper().center(50))
    print("═" * 50)


def customer_interface(username):
    print("\n" + "═" * 60)
    print(f"{username.capitalize()}, Welcome to our Restaurant ".upper().center(50))
    customer_menu()

def customer_menu():
    print("Customer Menu".center(60))
    print("═" * 60)
    print("1. View Menu")
    print("2. Place Order")
    print("3. View My Orders")
    print("4. Delete Order")
    print("5. Pay for Orders")
    print("6. Logout (Exit)")

    user_selected = int(input("Enter your choice: "))
    match user_selected:
        case 1:
            view_menu()
        case 2:
            ""
        case 3:
            ""
        case 4:
            exit()