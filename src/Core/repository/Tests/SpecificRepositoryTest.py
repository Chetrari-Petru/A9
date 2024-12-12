import unittest
from src.Core.repository.SpecificRepository import *

class TestObject:
    __id = None
    value = None
    def __init__(self, id, value):
        self.__id = id
        self.value = value

    def get_id(self):
        return self.__id

class GeneralRepositoryTests(unittest.TestCase):
    """
    it runs the tests from up to bottom
    """


    def test_storage_initialization(self):
        """
        Tests if it initializes the storage correctly
        """
        self.assertEqual(len(self.Repository.get_storage()), 0)  # add assertion here

    def test_add_element(self):
        """
        Tests if it adds an element to the storage correctly
        """
        self.Repository.add(value = self.items_to_be_added[0])
        self.assertEqual(self.Repository.get_storage()[1].value, self.items_to_be_added[0])

    def test_remove_element(self):
        """
        Tests if it removes an element from the storage correctly
        """
        self.test_add_element()
        self.Repository.remove(id = 1)
        self.assertEqual(len(self.Repository.get_storage()), 0)

    def setUp(self):
        """
        Sets up the test cases with an empty repository
        :return:
        """
        self.Repository = SpecificRepository(TestObject)
        self.items_to_be_added = [4]



if __name__ == '__main__':
    unittest.main()
