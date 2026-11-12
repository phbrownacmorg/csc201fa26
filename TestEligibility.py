import unittest
# Import the code you want to test here
from eligibility import *

class TestEligibility(unittest.TestCase):

    # When the code is run, it will run every method that begins with "test"
    def testEligibleHR_30_10(self) -> None: # generic "true" in age
         self.assertTrue(eligibleHR(30, 10))

    def testEligibleHR_25_10(self) -> None: # bottom boundary "true" in age
         self.assertTrue(eligibleHR(25, 10))

    def testEligibleHR_24_10(self) -> None: # top boundary "false" in age
         self.assertFalse(eligibleHR(24, 10))

    def testEligibleHR_20_10(self) -> None: # generic "false" in age
         self.assertFalse(eligibleHR(20, 10))

    def testEligibleHR_0_0(self) -> None: # bottom boundary "false" in age
         self.assertFalse(eligibleHR(0, 0))

    def testEligibleHR_n1_n1(self) -> None: # top boundary case, negative age
        with self.assertRaises(ValueError) as cm:
            eligibleHR(-1, -1)
        exc = cm.exception
        self.assertEqual(exc.args[0], 'Age cannot be negative.')

    # Age <= citizenship
    def testEligibleHR_30_30(self) -> None: # age == cit boundary of OK zone
        self.assertTrue(eligibleHR(30, 30))

    def testEligibleHR_30_31(self) -> None: # age < cit boundary of error zone
        with self.assertRaises(ValueError) as cm:
            eligibleHR(30, 31)
        exc = cm.exception
        self.assertEqual(exc.args[0], 'Years of citizenship cannot be greater than age.')
    

if __name__ == '__main__':
    unittest.main()

