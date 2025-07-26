from modules.crud import admin_add_user, view_staff, update_profile, update_user_profile, delete_user_profile

USER_FILE = 'data/users.txt'

def manage_staff(username):
    print("\n" + "═" * 50)
    print("Manage Staff Interface".center(50))
    print("═" * 50)
    print("1. Add New staff")
    print("2. View All Staff")
    print("3. Update Staff Profile")
    print("4. Delete Staff Profile")
    print("5. Back to Admin Panel")
    admin_choose = int(input("choose a option: "))
    match admin_choose:
        case 1:
            admin_add_user(username)
        case 2:
            view_staff(username)
        case 3:
            update_user_profile(username)
        case 4:
            delete_user_profile()
        case 5:
            print("\n" + "═" * 50)
            admin_interface(username)


def view_sales_report():
    print("View Sales Report")

def view_feedback():
    print("View Feedback")

def greeting_interface(username):
    print("\n" + "═" * 50)
    print(f"{username.upper()}, Welcome to the Restaurant Management System ".center(50))
    admin_interface(username)


def admin_interface(username):
    from modules.auth import auth_interface
    print("Admin Panel ".center(50))
    print("═" * 50)
    print("1. Manage Staff")
    print("2. View Sales Report")
    print("3. View Feedback")
    print("4. Update Profile")
    print("5. Log out (Exit)")
    admin_choose = int(input("Choose an option: "))
    match admin_choose:
        case 1:
            manage_staff(username)
        case 2:
            view_sales_report()
        case 3:
            view_feedback()
        case 4:
            update_profile(username)

        case 5:
            auth_interface()
