import unittest
import os

from src.Core.Errors.RepositoryErrors import NothingImportedError
from src.Core.repository.SpecificBinaryRepository import SpecificBinaryRepository

class TestObject:
    __id = None
    value = None
    def __init__(self, value, id):
        self.__id = id
        self.value = value

    def __dict__(self):
        return {"id":self.__id, "value":self.value}

    def __repr__(self):
        return str(self.__dict__())

    def get_id(self):
        return self.__id

class SpecificBinaryRepositoryTest(unittest.TestCase):
    def test_init(self):
        self.assertEqual(len(self.Repository.get_storage()), 0)

    def test_add_remove(self):
        try:
            self.Repository.add(value = 13)
        except NothingImportedError:
            pass
        storage = self.Repository.get_storage()
        self.assertEqual(storage[1].get_id(), 1)
        self.assertEqual(storage[1].value, 13)
        self.Repository.remove(id = 1)
        self.assertEqual(len(self.Repository.get_storage()), 0)


    def setUp(self):
        self.filename = "test_repository.pik"
        self.Repository = SpecificBinaryRepository(TestObject, os.path.join(os.getcwd(), self.filename))

    def tearDown(self):
        os.remove(self.filename)

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(os.path.join(os.getcwd(), 'TestsTemp')):
            os.mkdir(os.path.join(os.getcwd(), 'TestsTemp'))
        os.chdir(os.path.join(os.getcwd(), 'TestsTemp'))

    @classmethod
    def tearDownClass(cls):
        test_dir = os.getcwd()
        for file in os.listdir(test_dir):
            os.remove(os.path.join(test_dir, file))  # Remove each file

        os.chdir("..")
        os.rmdir(test_dir)


if __name__ == '__main__':
    unittest.main()
