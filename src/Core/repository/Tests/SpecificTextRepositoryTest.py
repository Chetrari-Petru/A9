import unittest
import os
from src.Core.repository.SpecificTextRepository import SpecificTextRepository
from src.Core.Errors.RepositoryErrors import *


class TestObject:
    v1 = None
    v2 = None
    id = None
    def __init__(self, v1, v2, id):
        self.v1 = v1
        self.v2 = v2
        self.id = int(id)

    def __dict__(self):
        return {"id": self.id, "v1": self.v1, "v2": self.v2}

    def get_id(self):
        return self.id

def clean_file(file):
    with open(file, "w") as f:
        f.write("")

class SpecificTextRepositoryTest(unittest.TestCase):

    def test_init(self):
        """
        Tests if it initializes the storage correctly
        """
        self.assertEqual(len(self.Repository.get_storage()), 0)

    def test_add_remove(self):
        try:
            self.Repository.add(v1=2, v2=3)
        except NothingImportedError:
            pass

        storage = self.Repository.get_storage()

        self.assertEqual(storage[1].get_id(), 1)
        self.assertEqual(storage[1].v1, '2')
        self.assertEqual(storage[1].v2, '3')

        self.Repository.remove(1)
        self.assertEqual(len(self.Repository.get_storage()), 0)

    def setUp(self):
        """
        Sets up the test cases with an empty repository
        :return:
        """
        FOLDER_NAME = "TestsTemp"
        self.script_path = os.path.dirname(os.path.realpath(__file__))
        self.filename = "test_repository.csv"
        test_path = os.path.join(self.script_path, FOLDER_NAME)
        if not os.path.exists(test_path):
            os.mkdir(test_path)
        os.chdir(test_path)
        self.Repository = SpecificTextRepository(TestObject ,os.getcwd()+"\\"+self.filename)

    def tearDown(self):
        clean_file(os.path.join(os.getcwd(), self.filename))

    @classmethod
    def tearDownClass(cls):
        test_dir = os.getcwd()
        for file in os.listdir(test_dir):
            os.remove(os.path.join(test_dir, file))  # Remove each file

        os.chdir("..")
        os.rmdir(test_dir)



if __name__ == '__main__':
    unittest.main(exit = False)
