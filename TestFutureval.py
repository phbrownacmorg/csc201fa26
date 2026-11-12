import contextlib
import io
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

    def testCalcInvestment_1000_01_4(self) -> None:
        amounts: list[float] = calc_investment(1000.0, 0.01, 4)
        self.assertEqual(len(amounts), 5)
        expected: list[float] = [1000.0, 1010.0, 1020.1, 1030.301, 1040.60401]
        for i in range(len(amounts)):
            with self.subTest(i=i):
                self.assertAlmostEqual(amounts[i], expected[i])

    def testCalcInvestment_1000_05_4(self) -> None:
        amounts: list[float] = calc_investment(1000.0, 0.05, 4)
        self.assertEqual(len(amounts), 5)
        expected: list[float] = [1000.0, 1050.0, 1102.5, 1157.625, 1215.50625]
        for i in range(len(amounts)):
            with self.subTest(i=i):
                self.assertAlmostEqual(amounts[i], expected[i])
        

    def testPrintTable_1000_01_1(self) -> None:
        out = io.StringIO()
        msg = 'Period\tAmount\n' + ('-' * 30) + '\n'
        msg += '0\t$1000.0\n1\t$1010.0\n'
        with contextlib.redirect_stdout(out):
            print_table([1000.0, 1010.0])
        self.assertEqual(out.getvalue(), msg)

    def testPrintTable_1000_01_4(self) -> None:
        msg = 'Period\tAmount\n' + ('-' * 30) + '\n'
        msg += '0\t$1000.0\n1\t$1010.0\n2\t$1020.1\n3\t$1030.3\n4\t$1040.6\n'
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print_table([1000.0, 1010.0, 1020.1, 1030.301, 1040.60401])
        self.assertEqual(out.getvalue(), msg)
        
    def testPrintTable_1000_05_4(self) -> None:
        msg = 'Period\tAmount\n' + ('-' * 30) + '\n'
        msg += '0\t$1000.0\n1\t$1050.0\n2\t$1102.5\n3\t$1157.62\n4\t$1215.51\n'
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print_table([1000.0, 1050.0, 1102.5, 1157.625, 1215.50625])
        self.assertEqual(out.getvalue(), msg)

if __name__ == '__main__':
    unittest.main()

