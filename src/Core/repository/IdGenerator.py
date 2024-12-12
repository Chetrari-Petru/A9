from src.Core.Errors.IdGeneratorErrors import *
class IdGenerator:
    def __init__(self):
        self.__last_id = 0
        self.__unused_ids = []

    def generate_id(self):
        if len(self.__unused_ids) != 0:
            return self.__unused_ids.pop()
        self.__last_id += 1
        return self.__last_id

    def remove_id(self, id):
        if id > self.__last_id:
            raise IdNotFoundError("Id was not found")
        if id in self.__unused_ids:
            raise IdRemovedError("Id has already been removed")
        self.__unused_ids.append(id)

    def initialize_state(self, max_id, unused_ids):
        self.__unused_ids = unused_ids
        self.__last_id = max_id