from user import register, login
from tracker import add_expense, view_expenses, delete_expense, show_summary

def main():
    print("============================")
    print("   Personal Expense Tracker")
    print("============================")

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            register(username, password)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            if login(username, password):
                while True:
                    print(f"\n--- {username}'s Menu ---")
                    print("1. Add Expense")
                    print("2. View Expenses")
                    print("3. Delete Expense")
                    print("4. Summary")
                    print("5. Logout")
                    action = input("Choose: ")
                    if action == "1":
                        add_expense(username)
                    elif action == "2":
                        view_expenses(username)
                    elif action == "3":
                        delete_expense(username)
                    elif action == "4":
                        show_summary(username)
                    elif action == "5":
                        print("Logged out.")
                        break

        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()