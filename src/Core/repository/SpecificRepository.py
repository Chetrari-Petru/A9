from src.Core.repository.IdGenerator import IdGenerator

class SpecificRepository:
    def __init__(self, type_of_content, *args):
        """
        Creates a memory type repository.
        :param type_of_content: The classType of the desired objects to be stored in the repository.
        """
        self._storage = {}
        self._id_generator = IdGenerator()
        self._type_of_content = type_of_content
        self._last_created_object = None

    def gen_sample(self):
        self._storage = self._type_of_content.sample(20)

    def get_type_of_content(self):
        return self._type_of_content

    def get_storage(self):
        return self._storage.copy()

    def get_storage_list(self):
        return list(self._storage.values())

    def clear_storage(self):
        self._storage = {}

    def _create_item(self, **kwargs):
        return self._type_of_content(**kwargs)

    def add(self, **kwargs):
        """
            Adds an element to the storage
            :param kwargs: The parameters for the specific type of the repository
        """
        item = self._create_item(id = self._id_generator.generate_id(), **kwargs)
        self._storage[item.get_id()] = item
        self._last_created_object = item
        return item

    def remove(self, id):
        """
            Removes an element from the storage
            :param id: The id of the element to be removed
        """
        self._id_generator.remove_id(id)
        del self._storage[id]

    def modify(self, new_object):
        """
        Modifies an object from the storage
        :param new_object: the object to be modified
        """
        self._storage[new_object.get_id()] = new_object
