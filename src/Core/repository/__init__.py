import os
from src.Core.domain import *
from .SpecificRepository import SpecificRepository
from .SpecificTextRepository import SpecificTextRepository
from .SpecificBinaryRepository import SpecificBinaryRepository
from .services import *
import random


repository_types = [
    "memory",
    "text",
    "binary"
]


class RepositoryController:
    """
    It is the main api of the repository.
    """
    _repo_types = {
        "memory": SpecificRepository,
        "text": SpecificTextRepository,
        "binary": SpecificBinaryRepository
    }

    _extensions = {
        "" : "memory",
        ".csv" : "text",
        ".pik" : "binary"
    }


    def __init__(self, client_path, movie_path, rental_path):
        self.client_repo = self._repo_types[self._extensions[os.path.splitext(client_path)[1]]](Client, client_path)
        self.movie_repo = self._repo_types[self._extensions[os.path.splitext(movie_path)[1]]](Movie, movie_path)
        self.rental_repo = self._repo_types[self._extensions[os.path.splitext(rental_path)[1]]](Rental, rental_path)
        self.client_services = RepositoryServices(self.client_repo)
        self.movie_services = RepositoryServices(self.movie_repo)
        self.rental_services = RentalRepositoryServices(self.rental_repo)
        if self._extensions[os.path.splitext(client_path)[1]] == "memory":
            self.client_repo.gen_sample()
        if self._extensions[os.path.splitext(movie_path)[1]] == "memory":
            self.movie_repo.gen_sample()
        if self._extensions[os.path.splitext(rental_path)[1]] == "memory":
            self.rental_repo.gen_sample()
            rentals = self.rental_repo.get_storage()
            clients=  self.client_repo.get_storage_list()
            movies = self.movie_repo.get_storage_list()
            self.rental_repo.clear_storage()
            for i in rentals:
                rental = rentals[i]
                rental_dict = rental.__dict__()
                rental_dict["client_id"] = random.choice(clients).get_id()
                rental_dict["movie_id"] = random.choice(movies).get_id()
                del rental_dict["id"]
                self.rental_repo.add(**rental_dict)
            




__all__ = ["RepositoryController", "SpecificRepository", "SpecificTextRepository", "SpecificBinaryRepository",]
