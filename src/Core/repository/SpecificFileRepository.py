from src.Core.repository.SpecificRepository import SpecificRepository
from src.Core.Errors.RepositoryErrors import *
import os


class SpecificFileRepository(SpecificRepository):
    def __init__(self, type_of_content, path_to_repository):
        self.path_to_repository = path_to_repository
        super(SpecificFileRepository, self).__init__(type_of_content)
        try:
            self._test_for_empty_file()
        except FileNotFoundError:
            with open(self.path_to_repository, 'wb') as f:
                f.write(b'')
        except FileIsEmptyError:
            pass
        storage = self.get_storage()
        if storage != {}:
            _max = max(storage)
            unused_ids= []
            for i in range(1,_max+1):
                if i not in storage:
                    unused_ids.append(i)
            self._id_generator.initialize_state(_max, unused_ids)


    def get_storage(self):
        try:
            self.read()
        except FileIsEmptyError:
            return {}
        return super(SpecificFileRepository, self).get_storage()

    def add(self, **kwargs):
        """
        Adds an element to the repository.
        :param kwargs: The parameters for the specific type of the repository
        """
        nothing_imported = None
        try:
            self.read()
        except FileNotFoundError as fnf:
            pass
        except FileIsEmptyError as fie:
            pass

        item = super(SpecificFileRepository, self).add(**kwargs)
        self.write()
        return item

    def remove(self, id):
        """
            Removes an element from the storage
            :param id: The id of the element to be removed
        """
        self.read()
        super(SpecificFileRepository, self).remove(id)
        self.write()

    def _test_for_empty_file(self):
        if os.stat(self.path_to_repository).st_size == 0:
            raise FileIsEmptyError()

    def write(self):
        pass

    def read(self):
        pass

    def modify(self, new_object):
        self.read()
        super().modify(new_object)
        self.write()