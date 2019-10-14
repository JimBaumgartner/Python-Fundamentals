option = int(input(prompt))
​
    if option == 5:
        quit()
    elif option == 1: # View menu
        os.system("cls")
        print(manager.read_menu())
    elif option == 2: # Add item
        new_item_name = input("What is the item's name? ")
        new_item_price = float(input("What is the item's price? "))
        print(manager.create_item(new_item_name, new_item_price))
    elif option == 3: # Change item
        for i, item in enumerate(manager.current_menu.contents):
            print(f"{i}> {item}")
        which_item = int(input("Which item would you like to change? "))
        new_name = input(f"New name (or blank to leave as-is) ")
        new_price = input("New price (or blank to leave as-is) ")
        print(manager.change_item(which_item, new_name, new_price))
    elif option == 4: # Remove item
        pass
    else:
        pass
Collapse



