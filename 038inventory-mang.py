inventory = ["apple, 200kgs", "banana, 240 dozens", "cherry, 20kgs", "oranges, 30kgs"]
while True:
    print("\nChoose an option:")
    opt = input("1. View stock\n2. Add items\n3. Remove items\n4. Exit\nChoose an option from above: ")

    if opt == '1':
       
        print("Current Inventory:")
        print(inventory)

    elif opt == '2':
        
        print("Enter the item to add and its quantity.")
        a = input("Item name and units (e.g., 'grapes, 15kgs'): ")
        inventory.append(a)
        print("Updated Inventory:")
        print(inventory)

    elif opt == '3':
        
        h = input("Enter the exact item to remove from the list (e.g., 'banana, 240 dozens'): ")
        h = h.strip()
        for h in inventory:
            inventory.remove(h) 
            print("Updated Inventory:")
            print(inventory)
        else:
            print("Item not found in inventory.")

    elif opt == '4':
        
        print("Exiting program.")
        break  

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
