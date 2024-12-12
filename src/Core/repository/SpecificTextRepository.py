from src.Core.repository.SpecificFileRepository import SpecificFileRepository


class SpecificTextRepository(SpecificFileRepository):
    def __init__(self, type_of_content, path_to_repository):
        super().__init__(type_of_content, path_to_repository)

    def write(self):
        """
        Writes the memory to disk.
        :return:
        """
        with open(self.path_to_repository, "w") as f:
            file_text = ""
            for element in self.get_storage_list():
                element_dict = element.__dict__()
                for key in element_dict:
                    file_text += str(element_dict[key]) + ","
                file_text += "\n"

            f.write(file_text)


    def read(self):
        """
        reads the memory form disk.
        :return:
        """
        self._test_for_empty_file()

        with open(self.path_to_repository, "r") as f:

            empty_obj = object.__new__(self._type_of_content)
            schematic = empty_obj.__dict__()
            line = f.readline()
            EMPTY = ""
            while line != EMPTY:
                args = line.split(",")
                kwargs = dict(zip(schematic, args))
                item = self._create_item(**kwargs)
                self._storage[item.get_id()] = item
                line = f.readline()


