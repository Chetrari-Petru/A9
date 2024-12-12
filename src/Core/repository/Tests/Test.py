import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    # Create a test suite from all test cases in the module
    suite = unittest.TestLoader().loadTestsFromModule(__import__(__name__))

    # Run the tests with a test runner
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Perform any additional logic after the tests
    print("not exited")
