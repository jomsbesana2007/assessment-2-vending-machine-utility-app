# the items the vending machine is selling
vendingmachine_items =  {
    "Hot Drinks": {"A1": ("Americano", 3.50, 10),
                   "A2": ("Cappucino", 5.00, 0),
                   "A3": ("Mocha", 4.50, 10),
                   "A4": ("Matcha", 5.50, 10),
                   "A5": ("Spanish Latte", 5, 10),
                   "A6": ("Macchiato", 4.50, 10),},

    "Cold Drinks": {"B1": ("Iced Americano", 3.50, 10),
                    "B2": ("Iced Caramel Frappe", 5, 10),
                    "B3": ("Iced Vanilla Frappe", 5, 10),
                    "B4": ("Iced Matcha", 6, 10),
                    "B5": ("Iced Spanish Latte", 5.50, 0),
                    "B6": ("Iced Macchiato", 5, 10),},

    "Pastries": {"C1": ("Croissant", 7, 10),
                 "C2": ("Danish Pastry", 6, 10),
                 "C3": ("Mille-Feuille", 8.50, 10),
                 "C4": ("Baklava", 9, 0),
                 "C5": ("Eclair", 6.50, 10),
                 "C6": ("Macarons", 7, 10),}
}

# the main program loop that runs perpetually until the user exits the program
mainLoop = 'y'
while mainLoop == 'y':
    chosen_drinkDetails = None
    chosen_pastryDetails = None
    print("\nWelcome to FastBakery Vending Machine!")

    # asks if the user wants to have a combo of a pastry and drink or only the pastry itself
    while True:
        try:
            menu_preference = int(input("\nChoose below\n1 - Drinks with Pastries\n2 - Pastries Only\nEnter a number here: "))
            if menu_preference == 1 or menu_preference == 2:
                break
            else:
                # is printed when the user enters an invalid number
                print("Enter a valid number!")
        except ValueError:
            # is printed when the user enters a letter or anything that is not an integer
            print("Enter a number!")
    
    # loop where the user chooses their selection
    loopOne = True
    while loopOne:
        # if user wants drinks with pastries
        if menu_preference == 1:
            # the first while loop under loopOne asks the user which drink category the user likes and then checks if it's valid
            subLoopOne = True
            while subLoopOne:
                try:
                    drink_category = int(input("\nChoose below\n1 - Hot Drinks\n2 - Cold Drinks\nEnter a number here: "))
                    if drink_category == 1 or drink_category == 2:
                        break
                    else:
                        # is printed when the user enters an invalid number
                        print("Enter a valid number!")
                except ValueError:
                    # is printed when the user enters a letter or anything that is not an integer
                    print("Enter a number!")

            # the second while loop under loopOne asks the user which slot number of the drink they want to buy from
            subLoopTwo = True
            while subLoopTwo:
                # prints the menu for hot drinks
                if drink_category == 1:
                    print("\nHot Drinks Menu List")
                    print(f"\n{'Slot No.':<10} {'Product Name':<20} {'Price':<10} {'Units Left':<10}")
                    print('-'*50)
                    # source: ChatGPT, prompt: How do you access a nested dictionary?
                    for slot_number, menu_list in vendingmachine_items["Hot Drinks"].items():
                        print(f"{slot_number:<10} {menu_list[0]:<20} {menu_list[1]:<10} {menu_list[2]:<10}")
                    
                    # user inputs the slot number of the product they want to buy
                    chosen_drink = input("\nEnter slot number here (ex: A1): ")

                    # source: ChatGPT, prompt: How to access the price with the dictionary?
                    chosen_drinkDetails = vendingmachine_items["Hot Drinks"].get(chosen_drink)
                    

                    # checks if the product the user chose is available or the slot number of the product is valid
                    if chosen_drinkDetails:
                        drinkName, drinkPrice, drinkUnitQuantity = chosen_drinkDetails
                        if drinkUnitQuantity == 0:
                            print("This product is out of stock! Choose another product.")
                            continue
                        else:
                            while True:
                                # asks if the user wants to restart their selection or continue with the next part of the program
                                user_confirmation = input(f"\nYou're buying one {drinkName}!\nDo you want to restart your selection?\n'Y' for yes and 'N' for no\nEnter here: ")
                                if user_confirmation.lower() == 'y':
                                    # the user is brought back to the start of the loop
                                    loopOne = True
                                    # subLoopThree is set to false so that the pastry part of the combo selection won't run
                                    subLoopThree = False
                                    break
                                elif user_confirmation.lower() == 'n':
                                    # terminates the current while loop
                                    subLoopTwo = False
                                    break
                                else:
                                    print("Invalid input!")
                                    continue
                    else:
                        # is printed when the user enters an invalid number
                        print("Invalid slot number! Try again")
                    
                # prints the menu for cold drinks
                elif drink_category == 2:
                    print("\nCold Drinks Menu List")
                    print(f"\n{'Slot No.':<10} {'Product Name':<20} {'Price':<10} {'Units Left':<10}")
                    print('-'*50)
                    for slot_number, menu_list in vendingmachine_items["Cold Drinks"].items():
                        print(f"{slot_number:<10} {menu_list[0]:<20} {menu_list[1]:<10} {menu_list[2]:<10}")
                    
                    # user inputs the slot number of the product they want to buy
                    chosen_drink = input("\nEnter slot number here (ex: A1): ")

                    chosen_drinkDetails = vendingmachine_items["Cold Drinks"].get(chosen_drink)

                    # checks if the product the user chose is available or the slot number of the product is valid
                    if chosen_drinkDetails:
                        drinkName, drinkPrice, drinkUnitQuantity = chosen_drinkDetails
                        if drinkUnitQuantity == 0:
                            print("This product is out of stock! Choose another product.")
                            continue
                        else:
                            while True:
                                # asks if the user wants to restart their selection or continue with the next part of the program
                                user_confirmation = input(f"\nYou're buying one {drinkName}!\nDo you want to restart your selection?\n'Y' for yes and 'N' for no\nEnter here: ")
                                if user_confirmation.lower() == 'y':
                                    # the user is brought back to the start of the loop
                                    loopOne = True
                                    # subLoopThree is set to false so that the pastry part of the combo selection won't run
                                    subLoopThree = False
                                    break
                                elif user_confirmation.lower() == 'n':
                                    # terminates the current while loop
                                    subLoopTwo = False
                                    break
                                else:
                                    print("Invalid input!")
                                    continue
                    else:
                        # is printed when the user enters an invalid number
                        print("Invalid slot number! Try again")
            
            # the third while loop under loopOne asks for the slot number of the pastry the user wants after buying their drink 
            # in order to create a combo.
            subLoopThree = True
            while subLoopThree:
                # prints the menu for pastries
                print("\nPastries Menu List")
                print(f"\n{'Slot No.':<10} {'Product Name':<20} {'Price':<10} {'Units Left':<10}")
                print('-'*50)
                for slot_number, menu_list in vendingmachine_items["Pastries"].items():
                    print(f"{slot_number:<10} {menu_list[0]:<20} {menu_list[1]:<10} {menu_list[2]:<10}")
                
                # user inputs the slot number of the product they want to buy
                chosen_pastry = input("\nEnter slot number here (ex: A1): ")

                chosen_pastryDetails = vendingmachine_items["Pastries"].get(chosen_pastry)

                # checks if the product the user chose is available or the slot number of the product is valid
                if chosen_pastryDetails:
                    pastryName, pastryPrice, pastryUnitQuantity = chosen_pastryDetails
                    if pastryUnitQuantity == 0:
                        print("This product is out of stock! Choose another product.")
                        continue
                    else:
                        while True:
                            # asks if the user wants to restart their selection or continue with the next part of the program
                            user_confirmation = input(f"\nYou're buying one {pastryName}!\nDo you want to restart your selection?\n'Y' for yes and 'N' for no\nEnter here: ")
                            if user_confirmation.lower() == 'y':
                                # the user is brought back to the start of the loop
                                subLoopThree = True
                                break
                            elif user_confirmation.lower() == 'n':
                                # terminates the current while loop
                                subLoopThree = False
                                break
                            else:
                                print("Invalid input!")
                                continue
                else:
                    # is printed when the user enters an invalid number
                    print("Invalid slot number! Try again")
                    continue
            # terminates loopOne to run the payment component of the program
            break

        # if user wants only pastries
        elif menu_preference == 2:
            # prints the menu for pastries
            print("\nPastries Menu List")
            print(f"\n{'Slot No.':<10} {'Product Name':<20} {'Price':<10} {'Units Left':<10}")
            print('-'*50)
            for slot_number, menu_list in vendingmachine_items["Pastries"].items():
                print(f"{slot_number:<10} {menu_list[0]:<20} {menu_list[1]:<10} {menu_list[2]:<10}")
            
            # user inputs the slot number of the product they want to buy
            chosen_pastry = input("\nEnter slot number here (ex: A1): ")

            chosen_pastryDetails = vendingmachine_items["Pastries"].get(chosen_pastry)

            # checks if the product the user chose is available or the slot number of the product is valid
            if chosen_pastryDetails:
                pastryName, pastryPrice, pastryUnitQuantity = chosen_pastryDetails
                if pastryUnitQuantity == 0:
                    print("This product is out of stock! Choose another product.")
                    continue
                else:
                    while True:
                        # asks if the user wants to restart their selection or continue with the next part of the program
                        user_confirmation = input(f"\nYou're buying one {pastryName}!\nDo you want to restart your selection?\n'Y' for yes and 'N' for no\nEnter here: ")
                        if user_confirmation.lower() == 'y':
                            # the user is brought back to the start of loopOne
                            loopOne = True
                            break
                        elif user_confirmation.lower() == 'n':
                            # loopOne is set to false so that it can proceed to the payment component of the program
                            loopOne = False
                            # terminates the current while loop
                            break
                        else:
                            print("Invalid input!")
                            continue
            else:
                # is printed when the user enters an invalid number
                print("Invalid slot number! Try again")
    
    
    loopThree = True
    loopTwo = True

    # The payment loop
    while loopTwo:
        # the receipt for the total cost if the user is buying a drink and a pastry
        if chosen_pastryDetails and chosen_drinkDetails:
            drinkName, drinkPrice, drinkUnitQuantity = chosen_drinkDetails
            pastryName, pastryPrice, pastryUnitQuantity = chosen_pastryDetails
            totalPrice = drinkPrice + pastryPrice
            print(f"\nDetails of Your Purchase\n")
            print('-'*30)
            print(f"{'Product':<20} {'Price':<10}")
            print(f"{drinkName:<20} {drinkPrice:<10}")
            print(f"{pastryName:<20} {pastryPrice:<10}")
            print(f"{'Total:':<20} {totalPrice}")

            while True:
                try:
                    # asks if the user wants to restart or proceed to pay
                    user_confirmation = int(input("\nDo you want to:\n1 - Proceed to Payment\n2 - Restart your entire selection\n"))
                    # the user is then asked to pay the amount
                    if user_confirmation == 1:
                        while True:
                            try:
                                userPayment = int(input("\nEnter the amount of cash (only up to $30): "))
                                # checks if the user paid enough
                                if userPayment < totalPrice:
                                    print("Insufficient balance")
                                    continue
                                # checks if the user paid more than the accepted amount
                                elif userPayment > 30:
                                    print("You can only pay up to $30")
                                    continue
                                else:
                                    # calculates the change if the user paid more than the total cost
                                    remaining_change = userPayment - totalPrice

                                    # deducts drinkUnitQuantity of a specific product after the user had bought it
                                    # source: ChatGPT, prompt: How to write code that deducts items from the inventory?
                                    if drinkName in [item[0] for item in vendingmachine_items["Hot Drinks"].values()]:
                                        vendingmachine_items["Hot Drinks"][chosen_drink] = (drinkName, drinkPrice, drinkUnitQuantity - 1)

                                    elif drinkName in [item[0] for item in vendingmachine_items["Cold Drinks"].values()]:
                                        vendingmachine_items["Cold Drinks"][chosen_drink] = (drinkName, drinkPrice, drinkUnitQuantity - 1)

                                    vendingmachine_items["Pastries"][chosen_pastry] = (pastryName, pastryPrice, pastryUnitQuantity - 1)

                                    # indicates that the drink and pastry have been dispensed
                                    print(f"\nYour {drinkName} and {pastryName} have been dispensed. Enjoy!")
                                    # prints out the change
                                    print(f"Your change is ${remaining_change}.")
                                    break
                            except ValueError:
                                # is printed when the user enters a letter or anything that is not an integer
                                print("Enter a number!")
                            break
                        break
                    # this brings the user back to the beginning of the program where they can select other products
                    elif user_confirmation == 2:
                        mainLoop = 'y'
                        loopThree = False
                        break
                    # is printed when the user enters an invalid number
                    else:
                        print("Enter a valid number!")
                        continue
                except ValueError:
                    print("Enter a number!")
                break
        
        # the receipt for the total cost if the user is buying only a pastry
        elif chosen_drinkDetails == None:
            pastryName, pastryPrice, pastryUnitQuantity = chosen_pastryDetails
            print(f"\nDetails of Your Purchase\n")
            print('-'*30)
            print(f"{'Product':<20} {'Price':<10}")
            print(f"{pastryName:<20} {pastryPrice:<10}")
            print(f"{'Total:':<20} {pastryPrice}")

            while True:
                try:
                    user_confirmation = int(input("\nDo you want to:\n1 - Proceed to Payment\n2 - Restart your entire selection\n"))
                    if user_confirmation == 1:
                        while True:
                            try:
                                userPayment = int(input("\nEnter the amount of cash (only up to $30): "))
                                # checks if the user paid enough
                                if userPayment < pastryPrice:
                                    print("Insufficient balance")
                                    continue
                                # checks if the user paid more than the accepted amount
                                elif userPayment > 30:
                                    print("You can only pay up to $30")
                                    continue
                                else:
                                    # calculates the change if the user paid more than the total cost
                                    remaining_change = userPayment - pastryPrice
                                    # deducts drinkUnitQuantity of a specific product after the user had bought it
                                    vendingmachine_items["Pastries"][chosen_pastry] = (pastryName, pastryPrice, pastryUnitQuantity - 1)
                                    # indicates that the drink and pastry have been dispensed
                                    print(f"\nYour {pastryName} has been dispensed. Enjoy!")
                                    # prints out the change
                                    print(f"Your change is $ {remaining_change}.")
                                    break
                            except ValueError:
                                # is printed when the user enters a letter or anything that is not an integer
                                print("Enter a number!")
                            break
                        break
                    # this brings the user back to the beginning of the program where they can select other products
                    elif user_confirmation == 2:
                        mainLoop = 'y'
                        loopThree = False
                        break
                    # is printed when the user enters an invalid number
                    else:
                        print("Enter a valid number!")
                        continue
                except ValueError:
                    print("Enter a number!")
                break
        break
    
    # asks if the user wants to exit the vending machine program or continue using
    while loopThree:
        try:
            user_confirmation = int(input("\nDo you want to:\n1 - Continue using the vending machine?\n2 - Exit the vending machine\nEnter here: "))
            if user_confirmation == 1:
                # goes back to the loop
                mainLoop = 'y'
                break
            elif user_confirmation == 2:
                # exits the loop
                mainLoop = 'n'
                break
            else:
                print("Enter a valid number!")
        except ValueError:
            print("Enter a number!")
            continue