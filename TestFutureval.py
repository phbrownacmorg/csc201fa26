import unittest
# Import the code you want to test here
from futureval import *

class TestFutureval(unittest.TestCase):

    # When the code is run, it will run every method that begins with "test"
    def testNothing(self) -> None:
        self.assertTrue(True)

    def testCalcInvestment_1000_01_1(self) -> None:
        amounts: list[float] = calc_investment(1000.0, 0.01, 1)
        self.assertEqual(len(amounts), 2)
        self.assertAlmostEqual(amounts[0], 1000.0)
        self.assertAlmostEqual(amounts[1], 1010.0)

    def testCalcInvestment_1000_01_10(self) -> None:
        amounts: list[float] = calc_investment(1000.0, 0.01, 4)
        self.assertEqual(len(amounts), 5)
        expected: list[float] = [1000.0, 1010.0, 1020.1, 1030.301, 1040.60401]
        for i in range(len(amounts)):
            with self.subTest(i=i):
                self.assertAlmostEqual(amounts[i], expected[i])
        
if __name__ == '__main__':
    unittest.main()

