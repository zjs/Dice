from RollResult import RollResult
import random

class DiceSet:
    def __init__(self, count, sides, keep=None):
        self.count = count
        self.sides = sides
        self.keep = keep

    def roll(self):
        return RollResult([random.randint(1,self.sides) for i in range(0, self.count)],self.keep)
