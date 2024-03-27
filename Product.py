#create class for product. This will include object functionality & attributes
class Product:
    def __init__(self, productID, productPrice, productName, productQuantity):
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
        self.__productQuantity += amount
    def removeQuantity(self, amount):
        if self.__productQuantity - amount < 0:
            raise Exception("error product quantity exceeded given value")
        else:
            self.__productQuantity -= amount