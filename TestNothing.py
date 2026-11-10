import unittest
# Import the code you want to test here

class TestNothing(unittest.TestCase):

    # When the code is run, it will run every method that begins with "test"
    def testNothing(self) -> None:
         self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

