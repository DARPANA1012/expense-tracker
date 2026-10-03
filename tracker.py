expenses = []

while True:
    print("\n1. Add  2. View  3. Total  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        item = input("Item: ")
        amount = float(input("Amount: "))
        expenses.append((item, amount))
        print("Expense saved!")
    elif choice == "2":
        for item, amount in expenses:
            print(f"{item}: {amount}")
    elif choice == "3":
        print("Total:", sum(a for _, a in expenses))
    elif choice == "4":
        break