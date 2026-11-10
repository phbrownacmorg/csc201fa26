import random
import unittest
# Import the code you want to test here
from volleyball import *

class TestVolleyball(unittest.TestCase):

    # When the code is run, it will run every method that begins with "test"
    # The "setUp" function runs before each test.
    def setUp(self) -> None:
        random.seed(401)

    def testGameState_0_0_A(self):
        self.assertEqual(game_state(0, 0, True),
                         'Score: A: 0 B: 0  A is serving') 

    def testGameState_0_0_B(self):
        self.assertEqual(game_state(0, 0, False),
                         'Score: A: 0 B: 0  B is serving') 

    def testGameState_8_5_B(self):
        self.assertEqual(game_state(8, 5, False),
                         'Score: A: 8 B: 5  B is serving') 

    def testGameState_4_5_B(self):
        self.assertEqual(game_state(4, 5, False),
                         'Score: A: 4 B: 5  B is serving')

    def testServerWinsTrue(self):
        self.assertTrue(server_wins(1))

    def testServerWinsFalse(self):
        self.assertFalse(server_wins(0))

    def testGameOver_0_0_15(self):
        self.assertFalse(game_over(0, 0, 15))

    def testGameOver_14_7_15(self):
        self.assertFalse(game_over(14, 7, 15))

    def testGameOver_15_7_15(self):
        self.assertTrue(game_over(15, 7, 15))

    def testGameOver_13_15_15(self):
        self.assertTrue(game_over(13, 15, 15))

    def testGameOver_14_15_15(self):
        self.assertFalse(game_over(14, 15, 15))
    
    def testGameOver_14_16_15(self):
        self.assertTrue(game_over(14, 16, 15))

    def testGameOver_14_16_15(self):
        self.assertTrue(game_over(14, 16, 15))

    def testGameOver_35_36_25(self):
        self.assertFalse(game_over(35, 36, 25))

    def testGameOver_38_36_25(self):
        self.assertTrue(game_over(38, 36, 25))

    def testSimPtRally_0_0_T_0(self):
         # A (serving side) loses
        self.assertEqual(sim_pt_rally(0, 0, True, 0), (0, 1, False))

    def testSimPtRally_0_0_T_1(self):
         # A (serving side) wins
        self.assertEqual(sim_pt_rally(0, 0, True, 1), (1, 0, True))

    def testSimPtRally_0_0_F_0(self):
         # B (serving side) loses
        self.assertEqual(sim_pt_rally(0, 0, False, 0), (1, 0, True))

    def testSimPtRally_0_0_F_1(self):
         # B (serving side) wins
        self.assertEqual(sim_pt_rally(0, 0, False, 1), (0, 1, False))

    def testSimPtSideOut_0_0_T_0(self):
         # A (serving side) loses
        self.assertEqual(sim_pt_sideout(0, 0, True, 0), (0, 0, False))

    def testSimPtSideOut_0_0_T_1(self):
         # A (serving side) wins
        self.assertEqual(sim_pt_sideout(0, 0, True, 1), (1, 0, True))

    def testSimPtSideOut_0_0_F_0(self):
         # B (serving side) loses
        self.assertEqual(sim_pt_sideout(0, 0, False, 0), (0, 0, True))

    def testSimPtSideOut_0_0_F_1(self):
         # B (serving side) wins
        self.assertEqual(sim_pt_sideout(0, 0, False, 1), (0, 1, False))

    def testGameRallyA(self):
        self.assertTrue(rallyAWon(0.56, 0.5604))

    def testGameRallyB(self):
        self.assertFalse(rallyAWon(0.5, 0.56))

    def testGameSideOutA(self):
        self.assertTrue(sideOutAWon(0.56, 0.5604))

    def testGameSideOutB(self):
        self.assertFalse(sideOutAWon(0.5, 0.56))



if __name__ == '__main__':
    unittest.main()

