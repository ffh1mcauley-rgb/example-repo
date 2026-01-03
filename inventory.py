from time import sleep

#========The beginning of the class==========

class Shoe:

    # Constructor method
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost) # Sets parameter type on creation
        self.quantity = int(quantity) 
        self.forsale = False # Additional property of Shoe added
  
    def get_cost(self):
        
        # Returns the cost parameter of the chosen shoe 
        return self.cost

    def get_quantity(self):
        
        # Returns quantity of chosen shoe
        return self.quantity
    
    def on_sale(self):

        # Checks to see if forsale parameter has already been changed
        if self.forsale == False:
            # If not then it updates forsale to True
            self.forsale = True
            print(f"\nThe {self.product} is now on sale.")
        else:
            # If it has already changed then a print statement
            # reflects that
            print(f"\nThe {self.product} is already on sale.")

    def __str__(self):
        
        # Returns all data for a Shoe as a string in a readable fashion
        return f"{self.country} : {self.code} : {self.product} : \
{self.cost} : {self.quantity}" 

#=============Shoe list===========

shoe_list = [] # This is the iterable that all sorting and searching 
               # will be done through

#==========Functions outside the class==============

def read_shoes_data():

    # Reads data off of a file line by line and adds it to the
    # shoe_list. 
    holder_list = [] # This list holds each line from file before 
                     # it is formatted
    try:
        with open("inventory.txt", "r", encoding="utf-8") as file:

            for line in file:
                # Removes \n from each line
                temp = line.strip()
                # Adds each line to holder list
                holder_list.append(temp)
        # Removes first line from file since it just describes 
        # the file's layout
        holder_list.pop(0)

        # Splits each line into a list and re-adds the lists
        # to the holder_list 
        for index, terms in enumerate(holder_list):
            hold = terms.split(",")

            holder_list[index] = hold
        # Creates the Shoe objects and adds them to shoe_list
        # Also creates line_num variable for use in except block
        for i in holder_list:
            line_num = holder_list.index(i) + 2

            shoe = Shoe(i[0], i[1], i[2], i[3], i[4])
            shoe_list.append(shoe)

        print("\n'inventory.txt' has been successfully uploaded" 
        " to the database.")
    # Deals with issues with locating the file    
    except FileNotFoundError as error:
        print("The 'inventory.txt' file is not in the right location" 
        " or it has been mispelled. Please check error below. \n")
        print(error)
    # Deals with formatting issues within the file   
    except (IndexError, ValueError):
        print(f"There is a formatting issue with line {line_num}"
            " in 'inventory.txt' \nMake sure that it is formatted using" 
            " the guide in line 1.")
        
def capture_shoes():

    # This fnc runs a series of while loops to acquire all inputs
    # necessary to create a Shoe object

    while True:
        
        country = str(input("\nWhat country are the shoes from? : "))

        print(f"\nYou have input '{country}'. Is that correct?")
        # This section allows a user to check and correct typos within
        # their inputs
        valid_input = input("Yes / No : ").lower()
        # The if else deals with getting a yes or no confirmation
        # If yes it moves onto the next loop. If no or invalid input
        # it will ask again
        if valid_input != "yes" and valid_input != "no":
            print("\nNeither 'Yes' nor 'No' selected."
            "\nPlease try inputting a country again.")
            continue

        if valid_input == "no":
            print("\nNo worries! Let's try again.")
            continue
        else:
            break
                  
    while True: # Same as above
        
        code = str(input("\nWhat is the shoe product code? : "))

        print(f"\nYou have input '{code}'. Is that correct?")

        valid_input = input("Yes / No : ").lower()

        if valid_input != "yes" and valid_input != "no":
            print("\nNeither 'Yes' nor 'No' selected."
            "\nPlease try inputting a code again.")
            continue

        if valid_input == "no":
            print("\nNo worries! Let's try again.")
            continue
        else:
            break        

    while True: # Same as above
        
        product = str(input("\nWhat is the product name? : "))

        print(f"\nYou have input '{product}'. Is that correct?")

        valid_input = input("Yes / No : ").lower()

        if valid_input != "yes" and valid_input != "no":
            print("\nNeither 'Yes' nor 'No' selected."
            "\nPlease try inputting a product again.")
            continue

        if valid_input == "no":
            print("\nNo worries! Let's try again.")
            continue
        else:
            break        

    while True: # This loop needs a float as an input
                # It has a try except to deal with Value Errors
        try:
            cost = float(input("\nWhat is the cost of the product? : "))

            print(f"\nYou have input '{cost}'. Is that correct?")

            valid_input = input("Yes / No : ").lower()

            if valid_input != "yes" and valid_input != "no":
                print("\nNeither 'Yes' nor 'No' selected."
                "\nPlease try inputting a cost again.")
                continue

            if valid_input == "no":
                print("\nNo worries! Let's try again.")
                continue
            else:
                break
        except ValueError:
            print("\nPlease input a number for the cost!" 
            "\nNo currency symbols required.")

    while True: # This loop works the same as the cost loop
                # However it requires an integer input to function
        try:
            quantity = int(input("\nWhat is the product's quantity? : "))

            print(f"\nYou have input '{quantity}'. Is that correct?")

            valid_input = input("Yes / No : ").lower()

            if valid_input != "yes" and valid_input != "no":
                print("\nNeither 'Yes' nor 'No' selected."
                "\nPlease try inputting a quantity again.")
                continue

            if valid_input == "no":
                print("\nNo worries! Let's try again.")
                continue
            else:
                break
        except ValueError:
            print("\nPlease input a whole number for the quantity!")

    # Prints out all the data for the object
    print("\nAdding new shoe to Shoe List :  \n")
    sleep(1.5)
    print("_" * 50, "\n")
    print(f"Country  : {country}")
    print(f"Code     : {code}")
    print(f"Product  : {product}")
    print(f"Cost     : {cost}")
    print(f"Quantity : {quantity}")
    print("_" * 50)
    # Creates new Shoe object and adds it to the shoe_list
    shoe_list.append(Shoe(country, code, product, cost, quantity))

def view_all():

    # This fnc prints out a key for the sort_list and then prints out
    # each object's data 1 by 1
    print("\nPrinting out Database")
    sleep(1.5)
    print("\nCountry : Code :"     
    " Product : Cost : Quantity :") # This line explains the format
    print("_" * 70, "\n")           # of the to be printed data
    # Sorts list by product alphabetically
    shoe_list.sort(key=lambda shoe: shoe.product)  
    for shoe in shoe_list:
        print(shoe)

    print("_" * 70)

def re_stock():
    
    # Sorts the shoe_list by quantity from lowest to highest
    # Prints out which shoe has lowest quantity and how many there are
    # Allows the user to input extra copies to restock the object

    # Sorts the shoe_list
    shoe_list.sort(key=lambda shoe: shoe.quantity)

    try: # This try except is to deal with if there are no items in
         # the shoe list

         # Prints out the lowest quantity item
        print(
            f"\n{shoe_list[0].product} is the lowest quantity item. \
It has {shoe_list[0].quantity} copies left in stock.")

        while True: # Loops until the user gives a positive int
            try:    # then adds that to the object's quantity
                extra_copies = int(input(
                    "\nHow many copies would you like to add? : "))

                if extra_copies >= 0: # Stops negative inputs
                    shoe_list[0].quantity += extra_copies

                    print(
                        f"\n{shoe_list[0].product} now has \
{shoe_list[0].quantity} copies in stock!"
                        )
                    break
                else:
                    print("\nPlease enter a positive whole number!")
                    continue
            except ValueError:  # Loops back to ask for new number
                                # When non integer is entered
                print("\nPlease enter a positive whole number!")
                continue
    except IndexError: # If shoe_list is empty then 
        print("\nThere is currently no data to sort.")
        print("Please add some data to use this function!")

def search_shoe():

    # Requests a shoe code before linear searching shoe_list
    # for the inputted code. If found it will return that Shoe's data
    # If not, it will say that the Shoe Code is not in the database
    target = input("\nPlease enter the Shoe Code of desired shoe : ")
    result = None # This is a default value that only changes when 
                  # the target is found

    for shoe in shoe_list:  # Linear search of the shoe_list
        if shoe.code == target: # Tries to match input with list codes
            result = shoe_list.index(shoe)

    if result != None: # If target is found then it's data is printed
        print(f"\nPrinting out data for Shoe Code {target}")
        sleep(1)
        print("_" * 50, "\n")
        print(f"Country  : {shoe_list[result].country}")
        print(f"Code     : {shoe_list[result].code}")
        print(f"Product  : {shoe_list[result].product}")
        print(f"Cost     : {shoe_list[result].cost}")
        print(f"Quantity : {shoe_list[result].quantity}")
        print("_" * 50)

    else: # Prints when target is not found
        print(f"\nData for Shoe Code {target} not found.") 

def value_per_item():
    
    # Sorts the shoe_list by product alphabetically
    # Calculates total value per shoe which is = cost * quantity
    # Prints out each total value 1 by 1

    # Sorts the list
    shoe_list.sort(key=lambda shoe: shoe.product)

    print("\nTotal value for each shoe :")
    sleep(1)
    print("_" * 50, "\n")

    for shoe in shoe_list: # Calculates total value for each shoe
        total_value = shoe.cost * shoe.quantity
        # Prints each shoe 1 by 1 with it's total value
        print(f"{shoe.product} \nTotal Value : {total_value} \n")

    print("_" * 50)

def highest_qty():
    
    # Tries to sort the shoe_list by quantity in ascending order
    # Prints out highest quantity item makes on sale request
    # If yes then the forsale of the Shoe is updated to True
    # Prints out confirmation

    try: # Sorts the list
        shoe_list.sort(key=lambda shoe: shoe.quantity)
        # Returns the object with highest quantity
        print(
            f"\n{shoe_list[-1].product} is the highest quantity item. \
It has {shoe_list[-1].quantity} copies left in stock.")

        while True: # Loops until a yes or no is given to put item
                    # on sale
            put_on_sale = input(f"\nWould you like to put \
{shoe_list[-1].product} on sale? \nYes / No : ").lower()
            
            if put_on_sale == "yes":
                shoe_list[-1].on_sale() # Changes forsale of object
                break
            elif put_on_sale == "no":
                print(f"\n{shoe_list[-1].product} will not be put on sale.")
                break
            else:
                print("\nPlease enter a valid response (Yes / No).")
                continue
    except IndexError: # This deals with if shoe_list is empty
        print("\nThere is currently no data to sort.")
        print("Please add some data to use this function!")
        
#==========Main Menu=============

while True: # This loop keeps menu open until user closes it
    
    print("\nWelcome to your Shoe Database Menu!")
    # Prints out each user option
    sleep(0.1)
    print("\n1 : Add data from 'inventory.txt' to the database.")
    sleep(0.1)
    print("\n2 : Input shoe data to add new shoe to database.")
    sleep(0.1)
    print("\n3 : View all current shoes stored in database.")
    sleep(0.1)
    print("\n4 : Restock lowest quantity shoe in database.")
    sleep(0.1)
    print("\n5 : Put highest quantity shoe in database on sale")
    sleep(0.1)
    print("\n6 : Search for shoe in database by inputting shoe code.")
    sleep(0.1)
    print("\n7 : Display total value for each shoe in database.")
    sleep(0.1)
    print("\n8 : Exit database.")

    try: # Try except is used to deal with a user not entering a number
        # from 1 -> 8 into the menu
        user_input = int(input("\nPlease enter the number of your" 
        " chosen operation to continue : "))
        # Only triggers operations if input is positive int from 1-8
        if user_input > 0 and user_input < 9:
            # Executes operation based on user input
            if user_input == 1:
                print("\nAttempting to add data from file to database")
                sleep(1.5)
                read_shoes_data()
                print("\nReturning to database menu.")
                sleep(1)

            if user_input == 2:
                print("\nPlease enter the required data when prompted.")
                sleep(1.5)
                capture_shoes()
                print("\nReturning to database menu.")
                sleep(2)

            if user_input == 3:
                view_all()
                print("\nReturning to database menu.")
                sleep(3)
            
            if user_input == 4:
                print("\nChecking for lowest quantity item.")
                sleep(1.5)
                re_stock()
                print("\nReturning to database menu.")
                sleep(2)

            if user_input == 5:
                print("\nChecking for highest quantity item.")
                sleep(1.5)
                highest_qty()
                print("\nReturning to database menu.")
                sleep(2)
            
            if user_input == 6:
                search_shoe()
                print("\nReturning to database menu.")
                sleep(2)
            
            if user_input == 7:
                value_per_item()
                print("\nReturning to database menu.")
                sleep(3)

            if user_input == 8: # This user input will close program
                print("\nThanks for using the database.")
                sleep(1)
                print("\nGoodbye!")
                sleep(1)
                break
        else: # If a negative int is entered or an int greater than 8
              # It will print an error msg and loop back to menu
            print("\nPlease enter a valid input (a number from 1 -> 8)")
        sleep(3)
    except ValueError: # If input is not an integer, prints error msg
                       # and loops back to menu
        print("\nPlease enter a valid input (a number from 1 -> 8)")
        sleep(3)