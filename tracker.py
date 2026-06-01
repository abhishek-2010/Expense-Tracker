from storage import save_data, load_data
from datetime import date

CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Health", "Education", "Other"]

def add_expense(username):
    data = load_data(username)
    print("\nCategories:", ", ".join(CATEGORIES))
    category = input("Enter category: ").capitalize()
    if category not in CATEGORIES:
        category = "Other"
    description = input("Enter description: ")
    amount = float(input("Enter amount (₹): "))
    entry = {
        "date": str(date.today()),
        "category": category,
        "description": description,
        "amount": amount
    }
    data["expenses"].append(entry)
    save_data(username, data)
    print("Expense added!")

def view_expenses(username):
    data = load_data(username)
    expenses = data["expenses"]
    if not expenses:
        print("No expenses found.")
        return
    print(f"\n{'#':<4} {'Date':<12} {'Category':<12} {'Description':<20} {'Amount':>8}")
    print("-" * 60)
    for i, e in enumerate(expenses, 1):
        print(f"{i:<4} {e['date']:<12} {e['category']:<12} {e['description']:<20} ₹{e['amount']:>7.2f}")

def delete_expense(username):
    view_expenses(username)
    data = load_data(username)
    if not data["expenses"]:
        return
    try:
        num = int(input("\nEnter expense number to delete: ")) - 1
        removed = data["expenses"].pop(num)
        save_data(username, data)
        print(f"Deleted: {removed['description']}")
    except (IndexError, ValueError):
        print("Invalid selection.")

def show_summary(username):
    data = load_data(username)
    expenses = data["expenses"]
    if not expenses:
        print("No data to summarize.")
        return
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Spent: ₹{total:.2f}")
    print("\nBy Category:")
    category_totals = {}
    for e in expenses:
        category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]
    for cat, amt in sorted(category_totals.items(), key=lambda x: -x[1]):
        print(f"  {cat:<15} ₹{amt:.2f}")