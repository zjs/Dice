import unittest
from RollResult import RollResult

class SimpleRollResultTestCase(unittest.TestCase):
    def setUp(self):
        self.rollResult = RollResult([6])

    def testGetResults(self):
        assert self.rollResult.getResults() == [(6,True)]

    def testGetRolls(self):
        assert self.rollResult.getRolls() == [6]

    def testGetKeptRolls(self):
        assert self.rollResult.getKeptRolls() == [6]

    def testGetValue(self):
        assert self.rollResult.getValue() == 6

class MultipleRollResultTestCase(unittest.TestCase):
    def setUp(self):
        self.rollResult = RollResult([3,5,6])

    def testGetResults(self):
        assert self.rollResult.getResults() == [(3,True),(5,True),(6,True)]

    def testGetRolls(self):
        assert self.rollResult.getRolls() == [3,5,6]

    def testGetKeptRolls(self):
        assert self.rollResult.getKeptRolls() == [3,5,6]

    def testGetValue(self):
        assert self.rollResult.getValue() == 14

class SimpleKeptRollResultTestCase(SimpleRollResultTestCase):
    def setUp(self):
        self.rollResult = RollResult([6],1)

class OneOfTwoKeptRollResultTestCase(SimpleRollResultTestCase):
    def setUp(self):
        self.rollResult = RollResult([1,6],1)

    def testGetResults(self):
        assert self.rollResult.getResults() == [(1,False),(6,True)]

    def testGetRolls(self):
        assert self.rollResult.getRolls() == [1,6]

class OneOfThreeKeptRollResultTestCase(SimpleRollResultTestCase):
    def setUp(self):
        self.rollResult = RollResult([1,6,4],1)

    def testGetResults(self):
        assert self.rollResult.getResults() == [(1,False),(6,True),(4,False)]

    def testGetRolls(self):
        assert self.rollResult.getRolls() == [1,6,4]

class MultipleKeptRollResultTestCase(MultipleRollResultTestCase):
    def setUp(self):
        self.rollResult = RollResult([3,5,6],3)

class ThreeOfFourKeptRollResultTestCaseA(MultipleRollResultTestCase):
    def setUp(self):
        self.rollResult = RollResult([1,3,5,6],3)

    def testGetResults(self):
        assert self.rollResult.getResults() == [(1,False),(3,True),(5,True),(6,True)]

    def testGetRolls(self):
        assert self.rollResult.getRolls() == [1,3,5,6]

class ThreeOfFourKeptRollResultTestCaseB(MultipleRollResultTestCase):
    def setUp(self):
        self.rollResult = RollResult([3,5,1,6],3)

    def testGetResults(self):
        assert self.rollResult.getResults() == [(3,True),(5,True),(1,False),(6,True)]

    def testGetRolls(self):
        assert self.rollResult.getRolls() == [3,5,1,6]

class ThreeOfFourKeptRollResultTestCaseC(MultipleRollResultTestCase):
    def setUp(self):
        self.rollResult = RollResult([3,5,6,1],3)

    def testGetResults(self):
        assert self.rollResult.getResults() == [(3,True),(5,True),(6,True),(1,False)]

    def testGetRolls(self):
        assert self.rollResult.getRolls() == [3,5,6,1]

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SimpleRollResultTestCase, 'test'))
    suite.addTest(unittest.makeSuite(MultipleRollResultTestCase, 'test'))
    suite.addTest(unittest.makeSuite(SimpleKeptRollResultTestCase, 'test'))
    suite.addTest(unittest.makeSuite(MultipleKeptRollResultTestCase, 'test'))
    suite.addTest(unittest.makeSuite(OneOfTwoKeptRollResultTestCase, 'test'))
    suite.addTest(unittest.makeSuite(OneOfThreeKeptRollResultTestCase, 'test'))
    suite.addTest(unittest.makeSuite(ThreeOfFourKeptRollResultTestCaseA, 'test'))
    suite.addTest(unittest.makeSuite(ThreeOfFourKeptRollResultTestCaseB, 'test'))
    suite.addTest(unittest.makeSuite(ThreeOfFourKeptRollResultTestCaseC, 'test'))

    return suite

