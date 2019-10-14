from data_layer import Item, Menu

import manager


while True:
    prompt = """
    What would you like to do?

    1) View the menu    
    2) Add item to  menu
    3) Change Item
    4) Remove Item
    5) Exit
    >"""
    option = int(input(prompt))

    if option == 5:
        quit()
    elif option == 1:
        print(manager.read_menu()) # this is pulling from manager tab that was imported from above
    elif option == 2: # Add item
        new_item_name = input("What is the item's name? ")
        new_item_price = float(input("What is the item's price? "))
        print(manager.create_item(new_item_name, new_item_price))
    # elif option == 3: # Change item
    #     for i, item in enumerate(manager.current_menu.contents):
    #         print(f"{i}> {item}")
    #     which_item = int(input("Which item would you like to change? "))
    #     new_name = input(f"New name (or blank to leave as-is) ")
    #     new_price = input("New price (or blank to leave as-is) ")
    #     print(manager.change_item(which_item, new_name, new_price))
        
    
    elif option == 3:
        for i, item in enumerate(manager.current_menu.contents):
            print(f"{ i }> { item }")
        which_item = int(input("Which item would you like to edit? >"))
        new_item_name = input(f"Change Name  >")
        new_item_price= float(input(f"Change Price  is to? ) >"))

        print(manager.change_item(which_item, new_item_name, new_item_price))
    elif option == 4:
        print()
    else:
        pass



    

