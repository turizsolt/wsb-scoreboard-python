

class GoalType:
    Action = 1
    Center = 2
    Sniper = 2
    Deadeye = 4

class GameDuration:
    MIN = 60
    Basic = 10 * MIN
    Extra = 12 * MIN
    Super = 15 * MIN
    Ultimate = 20 * MIN
    GameDurationByQualityShoots = [Basic, Basic, Basic, Basic, Extra, Super, Ultimate]


class WsbScoreBoard:
    def __init__(self):
        self.__scores = [0, 0]
        self.__qualification_shoots = [0, 0]
        self.__timer = 0

    def addScore(self, team, score):
        self.__scores[team] += score

    def getScore(self, team):
        return self.__scores[team]

    def addQualificationShoot(self, team):
        self.__qualification_shoots[team] += 1

    def getQualificationShoots(self, team):
        return self.__qualification_shoots[team]

    def setTimer(self):
        self.__timer = GameDuration.GameDurationByQualityShoots[sum(self.__qualification_shoots)]

    def getTimer(self):
        return self.__timer
