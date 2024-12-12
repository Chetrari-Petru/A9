import random
class Client:
    __client_id = None
    name = None
    def __init__(self, name, id):
        """
        Creates a Client Object
        :param name: The name of the client
        :param id: The given id
        """
        self.__client_id = int(id)
        self.name = name


    def __dict__(self):
        return {"id":self.__client_id, "name":self.name}

    def __repr__(self):
        return str(self.__dict__())+"\n"

    def get_id(self):
        return self.__client_id

    def change_field(self, field, new_value):
        if field == "name":
            self.name = new_value

    @staticmethod
    def sample(number_of_samples):
        ls = []
        _rentals = clients.copy()
        for i in range(number_of_samples):
            obj = _rentals.pop(random.randint(0, len(_rentals) - 1))
            ls[obj.get_id()] = obj

        return ls

clients = [
    Client("EagerFox", 1),
    Client("KindTiger", 2),
    Client("KindWolf", 3),
    Client("SharpFox", 4),
    Client("BoldWolf", 5),
    Client("QuickBear", 6),
    Client("CalmLion", 7),
    Client("HappyOwl", 8),
    Client("BrightTiger", 9),
    Client("SlickEagle", 10),
    Client("QuickHawk", 11),
    Client("CalmShark", 12),
    Client("EagerPanther", 13),
    Client("SmartFox", 14),
    Client("SharpHawk", 15),
    Client("HappyPanther", 16),
    Client("BrightWolf", 17),
    Client("BoldLion", 18),
    Client("SlickBear", 19),
    Client("EagerEagle", 20),
    Client("CalmOwl", 21),
    Client("KindShark", 22),
    Client("QuickFox", 23),
    Client("HappyTiger", 24),
    Client("SmartPanther", 25),
    Client("BoldEagle", 26),
    Client("BrightLion", 27),
    Client("SharpPanther", 28),
    Client("EagerBear", 29),
    Client("SlickWolf", 30),
    Client("HappyHawk", 31),
    Client("CalmTiger", 32),
    Client("KindPanther", 33),
    Client("SharpEagle", 34),
    Client("QuickShark", 35),
    Client("BrightOwl", 36),
    Client("SmartBear", 37),
    Client("EagerShark", 38),
    Client("BoldFox", 39),
    Client("SlickLion", 40),
    Client("KindOwl", 41),
    Client("HappyBear", 42),
    Client("SharpWolf", 43),
    Client("SmartHawk", 44),
    Client("CalmPanther", 45),
    Client("EagerTiger", 46),
    Client("QuickLion", 47),
    Client("BoldShark", 48),
    Client("KindEagle", 49),
    Client("SlickFox", 50)
]



