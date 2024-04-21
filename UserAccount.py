#import necessary classes. Stack, linkedList
from LinkedList import LinkedList
from Stack import Stack

#create list of acceptable account types
#acceptable account types: guest, user, admin
acceptableAccountTypes = ["guest", "user", "admin"]

class UserAccount:

    #UserAccount attributes:
    #userName, password, balance, accountType, shoppingCart, cartHistory

    def __init__(self,
            userName,
            password,
            balance,
            accountType,
            shoppingCart = LinkedList(),
            cartHistory = Stack()):


        #Check if data types match correct data type for each attribute. if not
        #raise exception
        if isinstance(userName, str):
            self.__userName = userName
        else:
            raise Exception("userName is not of type string")


        if isinstance(password, str):
            self.__password = password
        else:
            raise Exception("password is not of type string")


        #convert balance to float. if it cannot convert, it is not a number &
        #exception will be thrown automatically
        float(balance)
        #do not let balance be lower than 0
        if balance < 0:
            raise Exception("Balance cannot be less than 0")
        else:
            self.__balance = balance

        #check if account type is acceptable account type. Acceptable account type given
        #from list above.
        if accountType in acceptableAccountTypes:
            self.__accountType = accountType
        else:
            raise Exception("account type is not acceptable\nAcceptable account types:"
                            "guest, user, admin")


        if isinstance(shoppingCart, LinkedList):
            self.__shoppingCart = shoppingCart
        else:
            raise Exception("shoppingCart is not of type LinkedList")


        if isinstance(cartHistory, Stack):
            self.__cartHistory = cartHistory
        else:
            raise Exception("cartHistory is not of type Stack")

    def get_user_name(self):
        return self.__userName
    def get_password(self):
        return self.__password
    def get_balance(self):
        return self.__balance
    def get_cart_history(self):
        return self.__cartHistory
    def get_shopping_cart(self):
        return self.__shoppingCart
    def get_account_type(self):
        return self.__accountType

    def set_user_name(self, newUserName):
        if isinstance(newUserName, str):
            self.__userName = newUserName
        else:
            raise Exception("userName is not of type string")
    def set_password(self, newPassword):
        if isinstance(newPassword, str):
            self.__password = newPassword
        else:
            raise Exception("password is not of type string")
    def set_shopping_cart(self, newShoppingCart):
        #check if parameter is of type linked list
        if isinstance(newShoppingCart, LinkedList):
            self.__shoppingCart = newShoppingCart
        else:
            raise Exception("shoppingCart is not of type LinkedList")
    def add_to_shopping_cart(self, element):
        self.__shoppingCart.add(element)
    def remove_from_shopping_cart(self, element):
        self.__shoppingCart.remove(element)
    def set_account_type(self, newAccountType):
        #check if parameter is acceptable account type
        if newAccountType in acceptableAccountTypes:
            self.__accountType = newAccountType
        else:
            raise Exception("account type is not acceptable\nAcceptable account types:"
                            "guest, user, admin")
    def set_cart_history(self, newCartHistory):
        #check if cart history is of type Stack
        if isinstance(newCartHistory, Stack):
            self.__cartHistory = newCartHistory
        else:
            raise Exception("Cart History is not of type Stack")
    def add_to_cart_history(self, element):
        self.__cartHistory.push(element)
    def remove_from_cart_history(self):
        self.__cartHistory.pop()

    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        #do not allow negative balance
        if self.__balance - amount >= 0:
            self.__balance -= amount
        else:
            raise Exception("Balance cannot go below 0")

    def __str__(self):
        string = ("UserName: " + str(self.__userName) +
               "\nPassword: " + str(self.__password) +
               "\nBalance: " + str(self.__balance) +
               "\nShopping Cart:\n" + str(self.__shoppingCart) +
               "\nCart History: \n" + str(self.__cartHistory) +
               "\nAccount Type: " + str(self.__accountType))
        return string