from modules.menu import view_order_menu

FILE_USER = 'data/users.txt'
FILE_MENU = 'data/menu.txt'

def update_profile():
    print('Updating profile')

def send_feedback():
    print("\n" + "═" * 50)
    print("Please drop your feedback below.".upper().center(50))
    print("═" * 50)


def customer_interface(username):
    print("\n" + "═" * 50)
    print("Customer Menu".center(50))
    print(f"{username.capitalize()}, Welcome to our Restaurant ".upper().center(50))
    print("═" * 50)
    print("1. View Menu & Order Food")
    print("2. Send Feedback")
    print("3. Update profile")
    print("4. Cancel")
    user_selected = int(input("Enter your choice: "))
    match user_selected:
        case 1:
            view_order_menu()
        case 2:
            send_feedback()
        case 3:
            update_profile()
        case 4:
            exit()