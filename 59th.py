""" Write a menu driven python progarm where the user can add items, remove , view and exit"""

cart = []

while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print("Item added.")

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print("Item removed.")
        else:
            print("Item not found.")

    elif choice == 3:
        print("Cart:", cart)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")