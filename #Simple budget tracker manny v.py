#Simple budget tracker
import locale
# Set US formatting
locale.setlocale(locale.LC_ALL, "")

def get_income():
    while True:
        income = input("Enter your monthly income: ")
        try:
            income = float(income)
            if income < 0:
                raise ValueError("Income cannot be negative.")
            return income
        except ValueError as e:
            print("Error:", e)


def get_expenses():
    expenses = []

    while True:
        expense = input("Enter an expense (or 0 or 'done' to stop): ")

        if expense == "0" or expense.lower() == "done":
            break

        try:
            expense = float(expense)
            if expense < 0:
                raise ValueError("Expense cannot be negative.")
            expenses.append(expense)
        except ValueError as e:
            print("Error:", e)

    return expenses


def main():
    print("This program calculates your monthly budget.\n")

    income = get_income()
    expenses = get_expenses()

    total_expenses = sum(expenses)
    remaining = income - total_expenses

    print("\n----- Budget Summary -----")
    print(f"Total Income:    ${income:,.2f}")
    print(f"Total Expenses:  ${total_expenses:,.2f}")
    print(f"Remaining Money: ${remaining:,.2f}")

    print("\nYour Expenses:")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {locale.currency(e, grouping=True)}")

    print("\nCompleted by, Manuel Vargas")


if __name__ == "__main__":
    main()
