import unittest
# Import the code you want to test here
from quadratic import *

class TestQuadratic(unittest.TestCase):

    # When the code is run, it will run every method that begins with "test"
    def testRoots_1_0_0(self) -> None:
        root1, root2 = find_roots(1, 0, 0)
        self.assertAlmostEqual(root1, 0)
        self.assertAlmostEqual(root2, 0)

    # Just checks whether a ValueError is raised
    def testRoots_1_2_3(self) -> None:
        with self.assertRaises(ValueError):
            root1, root2 = find_roots(1, 2, 3)

    # Checks whether a ValueError is raised, and asks further about the error
    def testRoots_1_2_3_details(self) -> None:
        with self.assertRaises(ValueError) as cm:
            root1, root2 = find_roots(1, 2, 3)
        exc = cm.exception
        self.assertEqual(exc.args[0], 'expected a nonnegative input, got -8.0')

if __name__ == '__main__':
    unittest.main()

