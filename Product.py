class Product:
    # Initialize product with an ID, Name, Price, & Quantity. If no quantity given, set to 0
    def __init__(self, product_id, product_name, product_price, product_quantity=0):
        self.__product_id = product_id
        self.__product_price = product_price
        self.__product_name = product_name
        self.__product_quantity = product_quantity

    # Add getters & setters for attributes
    def get_id(self):
        return self.__product_id

    def get_price(self):
        return self.__product_price

    def get_name(self):
        return self.__product_name

    def get_quantity(self):
        return self.__product_quantity

    # Methods to update quantity
    def add_quantity(self, amount):
        # Ensure the amount is an integer
        amount = int(amount)

        # Add amount to quantity
        self.__product_quantity += amount

    def remove_quantity(self, amount):
        # Ensure amount is an integer
        amount = int(amount)

        # If amount goes below 0, there's not enough products to sell. Raise exception
        if self.__product_quantity - amount < 0:
            raise Exception("Error: product quantity exceeded allowed value")
        else:
            # Remove amount from quantity
            self.__product_quantity -= amount

    def set_quantity(self, amount):
        if amount < 0:
            raise Exception("Error: quantity exceeded allowed value")
        else:
            self.__product_quantity = amount

    def set_name(self, newName):
        self.__product_name = newName

    def set_price(self, newPrice):
        if newPrice < 0:
            raise Exception("Error: Price cannot be negative")
        else:
            self.__product_price = newPrice

    # Update the toString method to display all attributes & their values
    def __str__(self):
        string = ("Product ID: " + str(self.__product_id) + "\nProduct Name: " + str(self.__product_name) +
                  "\nProduct Price: $" + str(self.__product_price) + "\nProduct Quantity: " + str(
            self.__product_quantity) + "\n\n")
        return string