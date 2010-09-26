import copy

class RollResult:
    results = []

    def __init__(self, rolls, keep = None, multiplier = 1):
        self.multiplier = multiplier

        if keep == None:
            self.results = [(roll, True) for roll in rolls]
        else:
            sortedRolls = copy.copy(rolls)
            sortedRolls.sort()
            sortedRolls.reverse()
            toKeep = sortedRolls[0:keep]

            kept = 0
            results = []
            for roll in rolls:
                try:
                    toKeep.index(roll)
                    results.append((roll,True))
                    toKeep.remove(roll)
                except ValueError:
                    results.append((roll,False))

            self.results = results

    def getMultiplier(self):
        return self.multiplier

    def getResults(self):
        return self.results

    def getRolls(self):
        return [roll for (roll,kept) in self.results]

    def getKeptRolls(self):
        return [roll for (roll,kept) in self.results if kept]

    def getValue(self):
        return self.multiplier*sum(self.getKeptRolls())
