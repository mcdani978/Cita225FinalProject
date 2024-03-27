#this program will store the main process of the project.
from Product import Product

#create empty dictionary to store products with their ID as a key & the object as the value. this INCLUDES the objects of the products
productDictionary = {}
#create empty list to store product names & organize the products. This DOES NOT INCLUDE the objects of the products
productList = []


def main():
    #loop main function.
    while True:
        print("\n\n\n\n1. Add product\n2. Remove product \n3. Update Product Quantity\n4. Add to Cart"
              "\n5. Remove from Cart\n6. Undo Remove from Cart\n7. Display Inventory\n8. Display Cart\n")

        #Max selection is the number of functionalities the user has to choose from.
        maxSelection = 8

        #gather user input
        userInput = askForUserInput("Please enter your Option: ", "int")

        #test if user input is in valid range of integers
        while userInput < 1 or userInput > maxSelection:
            print("Please enter a valid selection from 1 to " + str(maxSelection))
            userInput = askForUserInput("Please enter your Option: ", "int")

        #match functionality to the given input. functionalities are given by their number as listed above

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

#methods to add to main:
def addProduct():
    #this method should create a new product object with ID, Price, Name, & Quantity
    #ask user to enter values for a new product

    pID = askForUserInput("Please enter the product ID, or type -1 to exit: ", "int")

    #exit if input is negative
    if pID < 0:
        return

    #if ID already exists, ask user to enter a different ID
    while pID in productDictionary:
        print("ID already exists. Please enter a different ID")
        pID = askForUserInput("Please enter the product ID, or type -1 to exit: ", "int")
        # exit if input is negative
        if pID < 0:
            return

    pName = askForUserInput("Please enter the product Name,or type -1 to exit: ", "string")
    pName = pName.lower()

    #exit if input is negative
    if pName == "-1":
        return


    #if name already exists in productlist, ask user to enter a different name. this should igore case sensitivity
    while pName in productList:
        print("name already exists. Please enter a different name")
        pName = askForUserInput("Please enter the product Name, or type -1 to exit: ", "string")
        pName = pName.lower()

        # exit if input is negative
        if pName == "-1":
            return

    pPrice = askForUserInput("Please enter the product price, or type -1 to exit: ", "float")

    # exit if input is negative
    if pPrice < 0:
        return

    pQuantity = askForUserInput("Please enter the quantity of the product, or type -1 to exit: ", "int")

    # exit if input is negative
    if pQuantity < 0:
        return

    #create new obejct
    newProduct = Product(pID, pName, round(pPrice, 2), pQuantity)

    #add object to dictionary
    productDictionary[newProduct.getID()] = newProduct

    #add product name to list
    productList.append(newProduct.getName())

def removeProduct():
    #remove the product from the list & dictionary
    userInput = askForUserInput("Please enter the product ID you want to remove, or type -1 to exit: ", "int")

    if userInput < 0:
        return

    #check if item is in the dictionary. if not, ask user to enter a different value
    while userInput not in productDictionary:
        print("Product ID not found. Please enter a different ID")
        userInput = askForUserInput("Please enter the product ID you want to remove, or type -1 to exit: ", "int")
        if userInput < 0:
            return

    #store name of product in temp variable to remove from productList
    pName = productDictionary[userInput].getName()

    #remove product from list & dictionary
    productDictionary.pop(userInput)
    productList.remove(pName)

def updateProductQuantity():
    #remove the product from the list & dictionary
    userInput = askForUserInput("Please enter the product ID for the product you wish to update, or type -1 to exit: ", "int")

    if userInput < 0:
        return

    #check if item is in the dictionary. if not, ask user to enter a different value
    while userInput not in productDictionary:
        print("Product ID not found. Please enter a different ID")
        userInput = askForUserInput("Please enter the product ID you want to remove, or type -1 to exit: ", "int")
        if userInput < 0:
            return

    #ask user for new quantity for the product
    newQuantity = askForUserInput("please enter the new quantity of the product: ", "int")

    if newQuantity < 0:
        return

    while newQuantity < 0:
        print("Invalid quantity. Please enter a positive integer")
        newQuantity = askForUserInput("please enter the new quantity of the product, or type -1 to exit", "int")
        if newQuantity < 0:
            return

    #update quantity of the product
    productDictionary[userInput].setQuantity(newQuantity)

def addToCart():
    return

def removeFromCart():
    return

def undoRemoveFromCart():
    return

def displayInventory():
    for key in productDictionary:
        print(productDictionary[key])
        print()


def displayCart():
    return

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
            testInput = userInput.replace("-", "")

            # Check if user input is a number. if not, make them enter a valid number
            while not testInput.isdigit():
                print("Please enter a valid number")
                userInput = input(strMessage)
                testInput = userInput.replace(".", "")
            return float(userInput)
        case __:
            raise Exception("Error: 'type' argument is invalid")


main()