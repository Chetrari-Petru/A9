import datetime
import random
class Rental:
    __movie_id = None
    __client_id = None
    __rented_date = None
    due_date = None
    returned_date = None
    __rental_id = None
    
    def __init__(self, movie_id, client_id, rented_date, due_date, returned_date, id):
        """
        Creates a new Rental object.
        :param movie_id: The id of the movie.
        :param client_id: The id of the client.
        :param rented_date: The date it is rented.
        :param due_date: The date it is due.
        :param returned_date: The date it is returned.
        :param id: The given id
        """
        self.__movie_id = int(movie_id)
        self.__client_id = int(client_id)
        self.__rented_date = rented_date
        self.due_date = due_date
        self.returned_date = returned_date
        self.__rental_id = int(id)


    def __dict__(self):
        return {"id": self.__rental_id,
                "movie_id": self.__movie_id,
                "client_id": self.__client_id,
                "rented_date": self.__rented_date,
                "due_date": self.due_date,
                "returned_date": self.returned_date}

    def __repr__(self):
        return str(self.__dict__())+"\n"

    def get_movie_id(self):
        """
        Returns the movie id
        :return: The id of the movie
        """
        return self.__movie_id

    def get_client_id(self):
        """
        Returns the client id
        :return: The id of the client
        """
        return self.__client_id

    def get_rented_date(self):
        """
        Returns the rented date
        :return: The date it is rented
        """
        return self.__rented_date

    def change_field(self, field, new_value):
        if field == "rented_date":
            self.__rented_date = new_value

        if field == "returned_date":
            self.__returned_date = new_value

        if field == "due_date":
            self.__due_date = new_value


    def get_id(self):
        return self.__rental_id

    @staticmethod
    def sample(number_of_samples):
        ls = {}
        _rentals = rentals.copy()
        for i in range(number_of_samples):
            obj = _rentals.pop(random.randint(0, len(_rentals) - 1))
            ls[obj.get_id()] = obj

        return ls

rentals = [
    Rental(12, 23, datetime.date(2023, 6, 15), datetime.date(2023, 6, 25), datetime.date(2023, 6, 20), 1),
    Rental(8, 45, datetime.date(2022, 3, 10), datetime.date(2022, 3, 20), None, 2),
    Rental(25, 32, datetime.date(2021, 8, 5), datetime.date(2021, 8, 15), datetime.date(2021, 8, 12), 3),
    Rental(18, 9, datetime.date(2023, 4, 22), datetime.date(2023, 5, 2), datetime.date(2023, 4, 30), 4),
    Rental(33, 19, datetime.date(2020, 11, 1), datetime.date(2020, 11, 11), datetime.date(2020, 11, 5), 5),
    Rental(40, 8, datetime.date(2024, 1, 15), datetime.date(2024, 1, 25), None, 6),
    Rental(5, 22, datetime.date(2023, 7, 18), datetime.date(2023, 7, 30), datetime.date(2023, 7, 28), 7),
    Rental(17, 11, datetime.date(2021, 2, 28), datetime.date(2021, 3, 10), None, 8),
    Rental(9, 33, datetime.date(2022, 12, 12), datetime.date(2022, 12, 22), datetime.date(2022, 12, 18), 9),
    Rental(4, 50, datetime.date(2020, 6, 8), datetime.date(2020, 6, 18), datetime.date(2020, 6, 10), 10),
    Rental(27, 2, datetime.date(2023, 11, 14), datetime.date(2023, 11, 24), None, 11),
    Rental(3, 48, datetime.date(2020, 10, 30), datetime.date(2020, 11, 9), datetime.date(2020, 11, 6), 12),
    Rental(49, 16, datetime.date(2021, 7, 19), datetime.date(2021, 7, 29), None, 13),
    Rental(2, 40, datetime.date(2022, 5, 25), datetime.date(2022, 6, 4), datetime.date(2022, 5, 30), 14),
    Rental(44, 13, datetime.date(2023, 8, 9), datetime.date(2023, 8, 19), datetime.date(2023, 8, 14), 15),
    Rental(7, 1, datetime.date(2020, 3, 3), datetime.date(2020, 3, 13), datetime.date(2020, 3, 7), 16),
    Rental(29, 21, datetime.date(2024, 4, 5), datetime.date(2024, 4, 15), None, 17),
    Rental(15, 31, datetime.date(2021, 6, 20), datetime.date(2021, 6, 30), datetime.date(2021, 6, 25), 18),
    Rental(41, 7, datetime.date(2022, 9, 17), datetime.date(2022, 9, 27), datetime.date(2022, 9, 22), 19),
    Rental(19, 37, datetime.date(2020, 12, 25), datetime.date(2021, 1, 4), None, 20),
    Rental(1, 5, datetime.date(2024, 2, 12), datetime.date(2024, 2, 22), None, 21),
    Rental(30, 6, datetime.date(2020, 8, 15), datetime.date(2020, 8, 25), datetime.date(2020, 8, 19), 22),
    Rental(6, 12, datetime.date(2023, 5, 5), datetime.date(2023, 5, 15), datetime.date(2023, 5, 8), 23),
    Rental(14, 39, datetime.date(2021, 10, 28), datetime.date(2021, 11, 7), datetime.date(2021, 10, 30), 24),
    Rental(26, 28, datetime.date(2022, 4, 13), datetime.date(2022, 4, 23), datetime.date(2022, 4, 18), 25),
    Rental(23, 49, datetime.date(2020, 1, 10), datetime.date(2020, 1, 20), datetime.date(2020, 1, 14), 26),
    Rental(11, 41, datetime.date(2023, 9, 2), datetime.date(2023, 9, 12), datetime.date(2023, 9, 6), 27),
    Rental(22, 14, datetime.date(2021, 3, 7), datetime.date(2021, 3, 17), None, 28),
    Rental(43, 26, datetime.date(2022, 7, 24), datetime.date(2022, 8, 3), datetime.date(2022, 7, 30), 29),
    Rental(13, 4, datetime.date(2020, 9, 19), datetime.date(2020, 9, 29), datetime.date(2020, 9, 24), 30),
    Rental(38, 36, datetime.date(2024, 5, 6), datetime.date(2024, 5, 16), None, 31),
    Rental(24, 18, datetime.date(2021, 11, 21), datetime.date(2021, 12, 1), datetime.date(2021, 11, 25), 32),
    Rental(48, 24, datetime.date(2022, 2, 9), datetime.date(2022, 2, 19), None, 33),
    Rental(10, 3, datetime.date(2020, 4, 11), datetime.date(2020, 4, 21), datetime.date(2020, 4, 15), 34),
    Rental(21, 35, datetime.date(2023, 12, 12), datetime.date(2023, 12, 22), None, 35),
    Rental(9, 10, datetime.date(2022, 1, 29), datetime.date(2022, 2, 8), datetime.date(2022, 2, 3), 36),
    Rental(35, 15, datetime.date(2021, 5, 4), datetime.date(2021, 5, 14), None, 37),
    Rental(31, 46, datetime.date(2022, 10, 23), datetime.date(2022, 11, 2), datetime.date(2022, 10, 28), 38),
    Rental(42, 20, datetime.date(2020, 2, 16), datetime.date(2020, 2, 26), None, 39),
    Rental(39, 44, datetime.date(2024, 6, 30), datetime.date(2024, 7, 10), None, 40),
    Rental(16, 38, datetime.date(2021, 12, 8), datetime.date(2021, 12, 18), datetime.date(2021, 12, 12), 41)
]
