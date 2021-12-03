# Programming Assignment 10.1: Your Own Class
# Madison Li
# flower_shop.py
# This program creates a class modeled after the real-world object, a flower shop. Upon instantiation, an object will have a randomized
# inventory, with each flower having 0-10 items in stock. The class will also have a "default inventory" which is referenced to refresh
# the inventory of any FlowerShop object. The main function of the class is to simulate purchasing flowers through the use of a shell.

import random # importing the random module in order to randomize the starting inventory of any particular FlowerShop object.

class FlowerShop:
    # CLASS ATTRIBUTE
    default_inventory = {"Calla Lily":10, "Rose":10, "Stargazer Lily":10, "Hydrangea":10, "Zinnia":10}
    # this default inventory can be accessed by any instance of the FlowerShop class

    # CONSTRUCTOR
    def __init__(self, name):
        # DATA ATTRIBUTES
        # stores the store name as a private attribute
        self.__name = name 
        # records the default types of flowers sold via a private attribute 
        self.__flowers = ["Calla Lily", "Rose", "Stargazer Lily", "Hydrangea", "Zinnia"] 
        # creates an empty variable for a potential new flower
        self.__special_flower = ""
        # the inventory is a private dictionary; keys: default types of flowers available. values: amount in stock
        self.__inventory = {} # constructs the starting inventory; the values/number in stock are randomized for each store
        for flower in self.__flowers: 
            self.__inventory.update({flower:int(random.randint(0, 10))})
        # assigns the default prices used to calculate total prices for the three purchasable options in the shop:
        # prices are 1) single flower 2) single flower in bouquet 3) price of vase
        self.__flower_price = 1.75 
        self.__bouquet_price = 1.50
        self.__vase_price = 4.00
        # boolean to flag whether the module has designated a "special offer", which is essentially adding a flower other than default
        self.__special_offer = False
    
    # METHODS
    # get_methods to access private attributes
    def get_name(self):
        '''Returns the current name of the FlowerShop object.'''
        return self.__name
    
    def get_flowers(self):
        '''Returns the default flowers of the FlowerShop object.'''
        return self.__flowers

    def get_inventory(self):
        '''Returns the current inventory of the FlowerShop object.'''
        return self.__inventory

    def get_flower_price(self):
        '''Returns the current price of a single flower within the FlowerShop object.'''
        return f"${self.__flower_price:.2f}"

    def get_bouquet_price(self):
        '''Returns the current price of a single flower within a bouquet in the FlowerShop object.'''
        return f"${self.__bouquet_price:.2f}"

    def get_vase_price(self):
        '''Returns the current price of a vase within the FlowerShop object.'''
        return f"${self.__vase_price:.2f}"

    # set_methods to change private attributes
    def set_name(self, name):
        '''Renames the FlowerShop object.'''
        self.__name = name

    def set_flower_price(self, price):
        '''Sets the price of a single flower within the FlowerShop object to a new value'''
        self.__flower_price = price

    def set_bouquet_price(self, price):
        '''Sets the price of a single flower within a bouquet in the FlowerShop object to a new value.'''
        self.__bouquet_price = price
    
    def set_vase_price(self, price):
        '''Sets the price of a vase within the FlowerShop object to a new value.'''
        self.__vase_price = price

    def set_amount(self, flower, amount):
        '''Sets the amount of stock for the specified flower to a new value. Flower cannot be a flower not already being sold.'''
        if type(amount) != int: # amount of stock must be an integer
            raise ValueError("Specified amount must be of int type.")
        elif flower not in self.__flowers: # checks if the flower is one of the default types
            # raises a ValueError and prints the associated error message if the flower is not a flower already being sold
            raise ValueError("This type of flower is not provided by the store.")  
        else:
            self.__inventory.update({flower:amount}) # if the flower is already being sold, updates the flower with the given amount

    def set_special_offer(self, flower, amount):
        '''Adds a new type of flower to the inventory, along with the specified stock. Flower cannot be a flower already being sold.
        Special offers will disappear after the inventory is refreshed.
        '''
        if flower not in self.__flowers: # checks if the flower is one of the default types
            self.__inventory.update({flower:amount}) # adds the flower as a new entry in the inventory
            self.__special_offer = True # since a new flower has been added, the boolean will indicate to the shell to post a message
            self.__special_flower = flower # stores the new flower so the shop shell can identify it later
        else:
            # raises a ValueError and prints the associated error message if the flower is a flower already being sold
            raise ValueError("This type of flower is already provided normally.")        

    # refresh method
    def refresh(self):
        '''Refreshes the FlowerShop's inventory to default.'''
        self.__inventory = self.default_inventory

    # display methods
    def display_prices(self):
        '''Displays the current prices for the FlowerShop object'''
        print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
        print("TODAY'S PRICES:")
        print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
        # uses the string syntax to format all the prices correctly
        # inserts the private attributes to ensure that prices will correspond to the values assigned, in case the set_methods were called previously
        print(f"Single Flower:\t${self.__flower_price:.2f}")
        print(f"Bouquet:\t{self.__bouquet_price:.2f} per flower")
        print(f"Bouquet w/ Vase:\t{self.__vase_price:.2f} + {self.__bouquet_price:.2f} per flower")

    def __str__(self):
        '''String magic method: displays the current inventory when the object is printed.'''
        str_rep = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\nFlower: Amount\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
        for flower, amount in self.__inventory.items(): # uses items() to iterate through both keys and values
            str_rep += f"{flower}: {amount}\n" # stores each flower and corresponding amount in a variable to be returned
        return str(str_rep) # casts as string to ensure that the __str__ magic method returns a string
    
    # shop method; a looping input shell
    def shop(self):
        '''A shell that simulates purchasing from a flower shop.'''
        total = 0 # local variable total to store total cost of customers' purchases
        flower_purchase = 0 # counts the number of times a single flower is purchased
        bouquet_purchase = 0 # counts the number of times a bouquet is purchased
        with_vase_purchase = 0 # counts the number of times a bouquet with a vase is purchased
        # uses the object's name data attribute to print a welcome message
        print(f"Welcome to {self.__name}! Here is our selection today: ")
        # displays randomized inventory to customer, as well as assigned prices
        print(self)
        self.display_prices()
        # if a new flower was added, the shop will announce it, and name the new flower
        if self.__special_offer == True:
            print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
            print("SPECIAL OFFER! A new flower will be sold until the inventory is refreshed. Stock limited.")
            print(f"The special flower is: {self.__special_flower}")
        # lists the available commands
        print("Available commands are help, buy, refresh, inventory, and checkout.")
        # starts the shell
        while True:
            command = input(">>> ")
            # conditional paths for each possible path; program will not exit until checkout is called
            if command == "help":
                # lists the available commands, as well as additional clarification
                print("Available commands are help, buy, refresh, inventory, and checkout.")
                print("The 'buy' command will prompt you for the specified item, and add that item to your cart.")
                print("The 'checkout' command will return the total cost of your purchases and exit the shell.")
                print("The 'refresh' command will restock the store. Keep in mind that any special offers will be ended.")
                print("The 'inventory' command will show you the store's current inventory.")
            elif command == "buy":
                # creates a new input loop to stay within the "buy" conditional path
                while True:
                    # try-except used to catch errors/incorrect commands within the loop
                    try: 
                        # int-casts to ensure that the paths work as intended
                        item = int(input("Which item would you like to buy?\nPlease input 1 for a single flower, 2 for a bouquet, and 3 for a bouquet with a vase. >>> "))
                        # if the customer buys a single flower:
                        if item == 1:
                            while True:
                                # allows the customer to select a flower
                                flower = input("Which flower would you like? >>> ")
                                # if the flower is out of stock, returns an error message and has the customer select again
                                if self.__inventory[flower] == 0:
                                    print("That flower is out of stock. Please try again.")
                                else:
                                    # adds the price of a single flower to the customer's total
                                    total += self.__flower_price
                                    # subtracts one from the specified flower's stock 
                                    self.__inventory.update({flower:(self.__inventory[flower]-1)})
                                    # prints a success message to the customer
                                    print("Your purchase was successfully added to your cart.")
                                    # increments the number of single-flower purchases
                                    flower_purchase += 1
                                    # prints the current total
                                    print(f"Current total: ${total:.2f}")
                                    break
                            break # exits both loops so the user can return to the start
                        # if the customer buys a bouquet:
                        elif item == 2:
                            # copies the inventory and total, since an incorrect command will require the customer to start their bouquet
                            # order over; this is done so that the price of the cancelled order will not be stored and carried to the end
                            temp_inventory = self.__inventory.copy() # the copy command is necessary in order to create a true copy
                            temp_total = 0
                            # creates a new input loop so that errors do not force the customer to select their type of order
                            while True:
                                try:
                                    # creates another input loop so that customers can select as many flowers as needed
                                    while True:
                                        flower = input("Which flower will you put in your bouquet? Type 'done' once you have selected all your flowers. >>> ")
                                        if flower == "done": # exits the loop if the customer types "done"
                                            break
                                        if temp_inventory[flower] == 0: # if the flower is out of stock, returns an error message and has the customer select again
                                            print("That flower is out of stock. Please try again.")
                                        else: # edits the temporary variables, adding on cost and decrementing inventory stock as needed
                                            temp_total += self.__bouquet_price
                                            temp_inventory.update({flower:(temp_inventory[flower]-1)})
                                    break # loop will only break if the order is successful
                                except:
                                    print("That is not a flower sold here. Please retype your full order.")
                                    # resets the temporary variables if an error occurs
                                    temp_inventory = self.__inventory
                                    temp_total = 0
                            # reassigns the temporary variables to the main variables once the purchase is successful
                            self.__inventory = temp_inventory.copy()
                            total += temp_total
                            # prints a success message to the customer
                            print("Your purchase was successfully added to your cart.")
                            # increments the number of bouquet purchases
                            bouquet_purchase += 1
                            # prints the current total
                            print(f"Current total: ${total:.2f}")
                            break # exits loop so the user can return to the start
                        # if the customer buys a bouquet with a vase
                        elif item == 3:
                            # code is largely the same as a normal bouquet purchase; only difference is an additional cost for the vase
                            temp_inventory = self.__inventory.copy()
                            temp_total = 0
                            while True:
                                try:
                                    while True:
                                        flower = input("Which flower will you put in your bouquet? Type 'done' once you have selected all your flowers. >>> ")
                                        if flower == "done":
                                            break
                                        if temp_inventory[flower] == 0:
                                            print("That flower is out of stock. Please try again.")
                                        else:
                                            temp_total += self.__bouquet_price
                                            temp_inventory.update({flower:(temp_inventory[flower]-1)})
                                    break
                                except:
                                    print("That is not a flower sold here. Please retype your full order.")
                                    temp_inventory = self.__inventory
                                    temp_total = 0
                            self.__inventory = temp_inventory.copy()
                            total += temp_total
                            total += self.__vase_price # adds the price of the vase to the purchase
                            # prints a success message to the customer
                            print("Your purchase was successfully added to your cart.")
                            # increments the number of bouquet with vase purchases
                            with_vase_purchase += 1
                            # prints the current total
                            print(f"Current total: ${total:.2f}")
                            break # exits loop so the user can return to the start
                    except: # catches any input that is not 1, 2, or 3, and allows the customer to try again
                        print("That is not a valid option. Please start again.")
            elif command == "refresh":
                # refreshes the inventory by calling the class's refresh method
                self.refresh()
                # prints a message to indicate a success
                print("Store has been refreshed!")
            elif command == "inventory":
                # calls the __str__ method, which prints out the current inventory
                print(self)
            elif command == "checkout":
                # returns the total cost, and the number of purchases for each category
                print(f"YOUR TOTAL IS: ${total:.2f}")
                print(f"individual flowers:\t{flower_purchase}")
                print(f"flower bouquets:\t{bouquet_purchase}")
                print(f"bouquets w/ vases:\t{with_vase_purchase}")
                print(f"Thank you for shopping with {self.__name}!")
                break # exits the program                        
            else: 
                # catches incorrect commands and allows the customer to try again
                print("That is not a valid command. For help on using the shell, input 'help'")  

def main():
    # creates the FlowerShop object
    shop = FlowerShop("Shelly's Flower Shop")
    # tests the get_methods
    print("================TESTING FLOWERSHOP GET_() METHODS================")
    print(f"[get_name()] This is the current name for the shop: {shop.get_name()}")
    print(f"[get_flowers()] These are the flowers sold: {shop.get_flowers()}")
    print(f"[get_inventory()] This is the current inventory: {shop.get_inventory()}")
    print(f"[get_flower_price()] This is the current price for a single flower: {shop.get_flower_price()}")
    print(f"[get_bouquet_price()] This is the current price for a flower in a bouquet: {shop.get_bouquet_price()}")
    print(f"[get_vase_price()] This is the current price for a vase: {shop.get_vase_price()}")
    # tests the set_methods
    print("================TESTING FLOWERSHOP SET_() METHODS================")
    shop.set_name("Madison's Flower Shop")
    shop.set_flower_price(2)
    shop.set_bouquet_price(1.8)
    shop.set_vase_price(6)    
    print(f"[set_name()] This is the new name for the shop: {shop.get_name()}")
    print("[set_flower_price(), set_bouquet_price(), set_vase_price()]")
    print(f"The new prices for flowers, flowers in bouquets, and vases are:\n{shop.get_flower_price()},\n{shop.get_bouquet_price()},\n{shop.get_vase_price()}")
    print(f"[set_amount()] Setting Zinnia amount to 15: ")
    shop.set_amount("Zinnia", 15)
    print(f"This is the current inventory: {shop.get_inventory()}")
    # tests the refresh method
    print("================TESTING FLOWERSHOP REFRESH() METHOD================")
    shop.refresh()
    print(f"This is the current inventory: {shop.get_inventory()}")
    # tests the special offer method
    print("================TESTING FLOWERSHOP SET_SPECIAL_OFFER() METHOD================")
    shop.set_special_offer("Carnation", 10)
    print(f"This is the inventory with the special offer, Carnation: {shop.get_inventory()}")
    # tests the display_price method
    print("================TESTING FLOWERSHOP DISPLAY_PRICE() METHOD================")
    shop.display_prices()
    # tests the __str__ magic method
    print("================TESTING FLOWERSHOP __STR__ METHOD================")
    print(shop)
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    # tests the shop shell
    # the shop shell is the main function of the class, and incorporates several methods within its commands, such as refresh() and __str__
    # the changes reflected in the past set_ commands will also be shown in the shell
    print("================TESTING FLOWERSHOP SHOP() METHOD================\n\n\n")
    shop.shop()

if __name__ == "__main__":
    main()