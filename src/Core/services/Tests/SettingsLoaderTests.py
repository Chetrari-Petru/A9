import unittest
from src.Core.services.SettingsLoader import SettingsLoader


class SettingsLoaderTests(unittest.TestCase):
    def test_init(self):
        self.assertTrue(True)

    def test_load(self):
        settings = self.loader.load_settings()
        print("nadsjk")
        print(settings)

    def setUp(self):
        self.loader = SettingsLoader()

if __name__ == '__main__':
    unittest.main()
