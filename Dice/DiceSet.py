from RollResult import RollResult
import random

class DiceSet:
    multiplier = 1
    count = 1
    sides = 1
    keep = 1

    def __init__(self, count, sides=1, keep=None):

        if count < 0:
            self.muliplier = -1
            self.count = -count
        else:
            self.muliplier = 1
            self.count = count

        self.sides = sides

        if keep == None:
            self.keep = count
        else:
            self.keep = keep

    def roll(self):
        return RollResult([random.randint(1,self.sides) for i in range(0, self.count)],self.keep,self.multiplier)
