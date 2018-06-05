import unittest
from WsbScoreBoard import WsbScoreBoard, GoalType

class GameDuration:
    Basic = 10*60
    Extra = 12*60
    Super = 15*60
    Ultimate = 20*60

class TestHello(unittest.TestCase):
    def setUp(self):
        self.wsbScoreBoard = WsbScoreBoard()

    def testAddAction(self):
        self.addScore(GoalType.Action, 1)

    def testAddCenter(self):
        self.addScore(GoalType.Center, 2)

    def testAddSniper(self):
        self.addScore(GoalType.Sniper, 2)

    def testAddDeadeye(self):
        self.addScore(GoalType.Deadeye, 4)

    def addScore(self, goalType, newScore):
        self.wsbScoreBoard.addScore(0, goalType)
        self.assertEqual(newScore, self.wsbScoreBoard.getScore(0))

    def testAddScoreSecondTeam(self):
        self.wsbScoreBoard.addScore(1, GoalType.Sniper)
        self.assertEqual(2, self.wsbScoreBoard.getScore(1))

    def testAddQualificationShoot(self):
        self.wsbScoreBoard.addQualificationShoot(0)
        self.wsbScoreBoard.addQualificationShoot(0)
        self.assertEqual(2, self.wsbScoreBoard.getQualificationShoots(0))

    def testAddQualificationShootSecondTeam(self):
        self.wsbScoreBoard.addQualificationShoot(1)
        self.assertEqual(1, self.wsbScoreBoard.getQualificationShoots(1))

    def testAddQualificationShootSecondTeam(self):
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.addQualificationShoot(0)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.assertEqual(3, self.wsbScoreBoard.getQualificationShoots(1))
       
    def testSetTimerAfter3QualificationShoots(self):
        self.wsbScoreBoard.addQualificationShoot(0)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.setTimer()
        self.assertEqual(GameDuration.Basic, self.wsbScoreBoard.getTimer())

    def testSetTimerAfter4QualificationShoots(self):
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.addQualificationShoot(0)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.setTimer()
        self.assertEqual(GameDuration.Extra, self.wsbScoreBoard.getTimer())

    def testSetTimerAfter5QualificationShoots(self):
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.addQualificationShoot(0)
        self.wsbScoreBoard.addQualificationShoot(0)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.setTimer()
        self.assertEqual(GameDuration.Super, self.wsbScoreBoard.getTimer())

    def testSetTimerAfter6QualificationShoots(self):
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.addQualificationShoot(0)
        self.wsbScoreBoard.addQualificationShoot(0)
        self.wsbScoreBoard.addQualificationShoot(0)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.addQualificationShoot(1)
        self.wsbScoreBoard.setTimer()
        self.assertEqual(GameDuration.Ultimate, self.wsbScoreBoard.getTimer())

    def testGetTimerWithoutSetTimer(self):
        self.assertEqual(0, self.wsbScoreBoard.getTimer())

    def testGetTimerWithoutSetTimerWithQS(self):
        self.wsbScoreBoard.addQualificationShoot(1)
        self.assertEqual(0, self.wsbScoreBoard.getTimer())



