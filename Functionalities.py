#class idea for storing functionalities for the program
class Functionalities:
    def __init__(self, name, text, permissions):
        self.__name = name
        self.__text = text
        if not isinstance(permissions, list):
            raise Exception("Error: permissions is not of type list")
        else:
            for element in permissions:
                if element not in ["guest", "user", "admin"]:
                    raise Exception("Error: permission is not of correct type")
                else:
                    self.__permissions = permissions

    def get_functionality_name(self):
        return self.__name
    def get_functionality_text(self):
        return self.__text
    def get_functionality_permissions(self):
        return self.__permissions