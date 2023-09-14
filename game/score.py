

class Score:
    def __init__(self,score,maxScore):
        self.score = score
        self.maxScore = maxScore
    def setMax(self,val):
        self.maxScore = val
    
    def updateScore(self,val):
        self.score += val
    
    def determineGrade(self):
        percentage = self.score / self.maxScore
        if percentage == 1:
            return "P"
        elif percentage >= 0.9:
            return "A"
        elif percentage >= 0.8:
            return "B"
        elif percentage >= 0.7:
            return "C"
        elif percentage >= 0.6:
            return "D"
        else:
            return "F"

score = Score(0,0)