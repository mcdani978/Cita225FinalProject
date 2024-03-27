#create class for product. This will include object functionality & attributes
class Product:
    #initialize product with an ID, Name, Price, & Quantity. If no quantity given, set to 0
    def __init__(self, productID, productName, productPrice, productQuantity = 0):
        self.__productID = productID
        self.__productPrice = productPrice
        self.__productName = productName
        self.__productQuantity = productQuantity

    #add getters & setters for attributes
    def getID(self):
        return self.__productID
    def getPrice(self):
        return self.__productPrice
    def getName(self):
        return self.__productName
    def getQuantity(self):
        return self.__productQuantity

    #methods to update quantity
    def addQuantity(self, amount):
        #ensure the amount is an integer
        amount = int(amount)

        #add amount to quantity
        self.__productQuantity += amount
    def removeQuantity(self, amount):
        #ensure amount is an integer
        amount = int(amount)

        #if amount goes below 0, there's not enough products to sell. Raise exception
        if self.__productQuantity - amount < 0:
            raise Exception("error product quantity exceeded allowed value")
        else:
            #remove amount from quantity
            self.__productQuantity -= amount
    def setQuantity(self, amount):
        if amount < 0:
            raise Exception("Error: quantity exceeded allowed value")
        else:
            self.__productQuantity = amount

    #update the toString method to display all attributes & their values
    def __str__(self):
        string = ("Product ID: " + str(self.__productID) + "\nProduct Name: " + str(self.__productName) +
              "\nProduct Price: $" + str(self.__productPrice) + "\nProduct Quantity: " + str(self.__productQuantity))
        return string