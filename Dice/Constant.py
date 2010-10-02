from RollResult import RollResult

class Constant:
    def __init__(self, value):
        self.value = value

    def roll(self):
        return RollResult([self.value])
