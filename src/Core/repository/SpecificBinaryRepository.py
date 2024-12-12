from src.Core.repository.SpecificFileRepository import SpecificFileRepository
import pickle


class SpecificBinaryRepository(SpecificFileRepository):
    def __init__(self, type_of_content, path_to_repository):
        super().__init__(type_of_content, path_to_repository)

    def write(self):
        """
        Writes the memory to disk.
        :return:
        """
        with open(self.path_to_repository, "wb") as file:

            stg = {}
            for key, value in self._storage.items():
                stg[key] = value.__dict__()
            pickle.dump(stg, file)

    def read(self):
        """
        Reads the memory from disk.
        :return:
        """
        self._test_for_empty_file()
        self._storage = {}

        with open(self.path_to_repository, "rb") as file:
            stg = pickle.load(file)
            for key, value in stg.items():
                self._storage[key] = self._type_of_content(**value)