# This program will store the main process of the project.
import tkinter as tk
from tkinter import simpledialog
from Product import Product
from LinkedList import LinkedList
from Stack import Stack
# Get the savedData.py file information
from savedData import *

# Add imports for GUI interface
from GUI import GUI

# Create empty dictionary to store products with their ID as a key & the object as the value.
# This INCLUDES the objects of the products
productDictionary = {}
# Create empty list to store product names & organize the products. This DOES NOT INCLUDE the objects of the products
productList = []
# Create empty linked list for shopping cart functionalities. This INCLUDES the product objects
shoppingCart = LinkedList()
# Create stack object to hold all additions and deletions from the cart. this INCLUDES the product objects
cartHistory = Stack()

def main():
    # Initialize the program information
    initializeProgram()

    # Ask the user for interface choice
    interface_choice = askForInterfaceChoice()

    # Launch GUI if choice is 1, otherwise continue with the command-line interface
    if interface_choice == 1:
        # Launch GUI interface
        root = tk.Tk()
        app = GUI(root, productDictionary, productList, shoppingCart, cartHistory)
        root.mainloop()
    elif interface_choice == 2:
        # Start command-line interface
        startCommandLineInterface()
    else:
        print("Invalid choice. Exiting program.")

def askForInterfaceChoice():
    while True:
        try:
            choice = int(input("Choose interface:\n1. GUI Interface\n2. Command Line Interface\nEnter choice: "))
            if choice not in [1, 2]:
                raise ValueError
            return choice
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

def startCommandLineInterface():
    # Loop main function
    while True:
        print("\n\n\n\n1. Add product\n2. Remove product \n3. Update Product Quantity\n4. Add to Cart"
              "\n5. Remove from Cart\n6. Undo Remove from Cart\n7. Display Inventory\n8. Display Cart\nDefault:"
              "Exit Program.\n")

        maxSelection = 8

        # Gather user input
        userInput = askForUserInput("Please enter your Option: ", "int")

        # Match functionality to the given input
        match userInput:
            case 1:
                addProduct()
            case 2:
                removeProduct()
            case 3:
                updateProductQuantity()
            case 4:
                addToCart()
            case 5:
                removeFromCart()
            case 6:
                undoRemoveFromCart()
            case 7:
                displayInventory()
            case 8:
                displayCart()
            case __:
                endProgram()
                return

#methods to add to main:
def addProduct():
    # This method should create a new product object with ID, Price, Name, & Quantity
    # Ask user to enter values for a new product
    pID = askForUserInput("Please enter the product ID, or type -1 to exit: ", "int")

    # Exit if input is negative
    if pID < 0:
        return

    # If ID already exists, ask user to enter a different ID
    while pID in productDictionary:
        print("ID already exists. Please enter a different ID")
        pID = askForUserInput("Please enter the product ID, or type -1 to exit: ", "int")
        # Exit if input is negative
        if pID < 0:
            return

    pName = askForUserInput("Please enter the product Name, or type -1 to exit: ", "string")
    pName = pName.lower()

    # Exit if input is negative
    if pName == "-1":
        return

    # If name already exists in productList, ask user to enter a different name. This should ignore case sensitivity
    while pName in productList:
        print("Name already exists. Please enter a different name")
        pName = askForUserInput("Please enter the product Name, or type -1 to exit: ", "string")
        pName = pName.lower()

        # Exit if input is negative
        if pName == "-1":
            return

    pPrice = askForUserInput("Please enter the product price, or type -1 to exit: ", "float")

    # Exit if input is negative
    if pPrice < 0:
        return

    pQuantity = askForUserInput("Please enter the quantity of the product, or type -1 to exit: ", "int")

    # Exit if input is negative
    if pQuantity < 0:
        return

    # Create new object
    newProduct = Product(pID, pName, round(pPrice, 2), pQuantity)

    # Add object to dictionary
    productDictionary[newProduct.getID()] = newProduct

    # Add product name to list
    productList.append(newProduct.getName())

def removeProduct():
    #remove the product from the list & dictionary
    userInput = askForUserInput("Please enter the product ID you want to remove, "
                                "or type -1 to exit: ", "int")

    if userInput < 0:
        return

    #check if item is in the dictionary. if not, ask user to enter a different value
    while userInput not in productDictionary:
        print("Product ID not found. Please enter a different ID")
        userInput = askForUserInput("Please enter the product ID you want to remove, "
                                    "or type -1 to exit: ", "int")
        if userInput < 0:
            return

    #store name of product in temp variable to remove from productList
    pName = productDictionary[userInput].getName()

    #remove product from list & dictionary
    productDictionary.pop(userInput)
    productList.remove(pName)

def updateProductQuantity():
    #remove the product from the list & dictionary
    userInput = askForUserInput("Please enter the product ID for the product you wish to update, "
                                "or type -1 to exit: ", "int")

    if userInput < 0:
        return

    #check if item is in the dictionary. if not, ask user to enter a different value
    while userInput not in productDictionary:
        print("Product ID not found. Please enter a different ID")
        userInput = askForUserInput("Please enter the product ID you want to remove, "
                                    "or type -1 to exit: ", "int")
        if userInput < 0:
            return

    #ask user for new quantity for the product
    newQuantity = askForUserInput("please enter the new quantity of the product: ", "int")

    if newQuantity < 0:
        return

    while newQuantity < 0:
        print("Invalid quantity. Please enter a positive integer")
        newQuantity = askForUserInput("please enter the new quantity of the product, "
                                      "or type -1 to exit", "int")
        if newQuantity < 0:
            return

    #update quantity of the product
    productDictionary[userInput].setQuantity(newQuantity)

def addToCart():
    #loop until the user doesn't want to continue shopping
    while True:
        #each node will be a Product added to the cart.
        #Display all products & let user choose product they want.
        for index in range(len(productList)):
            print(f"{index}. " + productList[index])
        userInput = askForUserInput("please choose an item you want to add to cart, "
                                    "or type -1 to exit", "int")

        if userInput < 0:
            return
        while userInput >= len(productList):
            print("Invalid input. Please choose one of the diplayed products, or type -1 to exit")
            for index in range(len(productList)):
                print(f"{index}. " + productList[index])
            userInput = askForUserInput("please choose an item you want to add to cart, "
                                        "or type -1 to exit", "int")
            if userInput < 0:
                return

        #find user option in productDictionary.
        for key in productDictionary:
            #store object in a temporary variable. Python doesn't like to behave sometimes
            tempObj = productDictionary[key]

            if tempObj.getName() == productList[userInput]:
                #check if the store has ran out of the product
                if tempObj.getQuantity() == 0:
                    print("Sorry, we are out of that product")
                    break; #no need to continue looping
                else:
                    # add to shopping cart
                    print("adding to cart...")
                    shoppingCart.add(tempObj)
                    #remove 1 quantity from the object
                    tempObj.removeQuantity(1)
                    break; #no need to continue looping

def removeFromCart():
    #loop until user doesn't want to remove a product
    while True:
        #remove first occurrence of an item from the cart, add 1 quantity back to the product, add action to cart history
        #create list showing products they can remove
        for index in range(len(productList)):
            print(f"{index}. " + productList[index])
        #ask user what they want to remove

        userInput = askForUserInput("What product from cart do you want to remove?, "
                                    "or type -1 to exit", "int")
        if userInput < 0:
            return
        while userInput >= len(productList):
            print("Invalid input. Please choose one of the diplayed products, or type -1 to exit")
            for index in range(len(productList)):
                print(f"{index}. " + productList[index])
            userInput = askForUserInput("please choose an item you want to add to cart, "
                                        "or type -1 to exit", "int")
            if userInput < 0:
                return

        #check if product is in cart. if not, do nothing, else, remove from cart & add action to history
        for key in productDictionary:
            if productList[userInput] == productDictionary[key].getName():
                #remove LAST occurrence of product from list
                if not shoppingCart.remove(productDictionary[key]):
                    print("item not in cart")
                else:
                    print("Removing...")
                    #add product back to shelf
                    productDictionary[key].addQuantity(1)
                    #add action to stack history
                    cartHistory.push(productDictionary[key])

def undoRemoveFromCart():
    #check if product is in stock before adding back to cart

    #store object in variable
    addBackToCart = cartHistory.pop()

    #check if item has been popped from cart
    if addBackToCart!= None:
        #check if product has been sold out
        if addBackToCart.getQuantity() > 0:
            #add back to cart
            print("adding to cart...")
            shoppingCart.add(addBackToCart)
            # remove 1 quantity from the object
            addBackToCart.removeQuantity(1)
        else:
            print(f"Sorry, we sold out of the product: {addBackToCart.getName()}")
    else:
        print("No action in history")

def displayInventory():
    for key in productDictionary:
        print(productDictionary[key])
        print()

def displayCart():
    #print the shopping cart
    print(shoppingCart)

def askForUserInput(strMessage, type):
    #store user input in a variable & check if all characters are digits
    userInput = input(strMessage)

    #print("type entered: " + type)

    match type:

        case "string":
            #print("returning a string")
            return userInput
        case "int":
            #print("returning an int")

            # replace "." in potential string with "" to better test string with isDigit() function
            # Credit for idea: https://pythonhow.com/how/check-if-a-string-is-a-float/
            testInput = userInput.replace(".", "")
            testInput = userInput.replace("-", "")
            #Check if user input is a number. if not, make them enter a valid number
            while not testInput.isdigit():
                print("Please enter a valid number")
                userInput = input(strMessage)
                testInput = userInput.replace(".", "")

                # check if user input is an integer. if not, that is it contains a "." in the number, repeat the function
                # for the user to enter an integer.
            if "." in userInput:
                print("Please enter an integer")
                userInput = askForUserInput(strMessage, type)
            return int(userInput)
        case "float":
            #print("returning a float")

            # replace "." in potential string with "" to better test string with isDigit() function
            # Credit for idea: https://pythonhow.com/how/check-if-a-string-is-a-float/
            testInput = userInput.replace(".", "")
            testInput = testInput.replace("-", "")

            #print("testinput:" + str(testInput))

            # Check if user input is a number. if not, make them enter a valid number
            while not testInput.isdigit():
                print("Please enter a valid number")
                userInput = input(strMessage)
                testInput = userInput.replace(".", "")
            return float(userInput)
        case __:
            raise Exception("Error: 'type' argument is invalid. Valid types:\nstring\nint\nfloat")



#initializeProgram will retrieve all data from savedData.py file to initialize the list, dictionary, shopping cart,
#and the cart history.
def initializeProgram():
    #set the productDictionary from dictionary information given by savedData.py
    #read each element in the 2-d list, create the object given the information, & store that in the dictionary
    for i in range(len(dictionaryInformation)):
        list = dictionaryInformation[i]
        pID = list[0]
        pName = list[1]
        pPrice = list[2]
        pQuantity = list[3]
        #create object
        tempObj = Product(pID,pName,pPrice,pQuantity)
        #send object to dictionary
        productDictionary[pID] = tempObj

    #set the productList from listInformation given by savedData.py
    for element in listInformation:
        productList.append(element)

    #set the shoppingCart from shoppingCartInformation given by savedData.py
    for row in shoppingCartInformation:
        #store info in respective variables
        pID = row[0]
        pName = row[1]
        pPrice = row[2]
        pQuantity = row[3]

        #create temporary object
        tempObj = Product(pID,pName,pPrice,pQuantity)
        #send object to shopping cart list
        shoppingCart.add(tempObj)

    #set the cartHistory from cartHistoryInformation given by savedData.py
    #reverse order of cartHistoryInformation. first in is last element in list
    cartHistoryInformation.reverse()
    for row in cartHistoryInformation:
        #store info in respective variables
        pID = row[0]
        pName = row[1]
        pPrice = row[2]
        pQuantity = row[3]

        #create temporary object
        tempObj = Product(pID,pName,pPrice,pQuantity)
        #send obejct to cartHistory
        cartHistory.push(tempObj)

#end program will save all user data to a python file. saved data will include the list, dictionary, shopping cart,
#and the cart history.
def endProgram():
    file = open("savedData.py", "w")

    #to save an object to the file, you need to get each attribute out of the object & send the information over.
    #data will be saved in a 2-d list. each row will save the obejct information & each column will contain
    #the product ID, name, price, and quanitity in that order

    #add productDictionary information
    objectList = []
    for key in productDictionary:
        pID = productDictionary[key].getID()
        pName = productDictionary[key].getName()
        pPrice = productDictionary[key].getPrice()
        pQuantity = productDictionary[key].getQuantity()

        objectList.append([pID,pName,pPrice,pQuantity])

    #write the dictionary information to the file
    file.write("dictionaryInformation = " + str(objectList) + "\n")

    #write product list to the file
    file.write("listInformation = " + str(productList) + "\n")

    #write the shopping cart information to the file
    shoppingCartInformation = []
    while not shoppingCart.isEmpty():
        shoppingCartObj = shoppingCart.removeLast()
        pID = shoppingCartObj.getID()
        pName = shoppingCartObj.getName()
        pPrice = shoppingCartObj.getPrice()
        pQuantity = shoppingCartObj.getQuantity()
        shoppingCartInformation.append([pID,pName,pPrice,pQuantity])

    #add shoppingCartInfo to the file
    file.write("shoppingCartInformation = " + str(shoppingCartInformation) + "\n")

    #add cart history to the shopping cart
    cartHistoryInformation = []

    while not cartHistory.isEmpty():
        cartHistoryObj = cartHistory.pop()
        pID = cartHistoryObj.getID()
        pName = cartHistoryObj.getName()
        pPrice = cartHistoryObj.getPrice()
        pQuantity = cartHistoryObj.getQuantity()
        cartHistoryInformation.append([pID,pName,pPrice,pQuantity])
    #write cartHistory info to file
    file.write("cartHistoryInformation = " + str(cartHistoryInformation) + "\n")
    #close the file
    file.close()

main()