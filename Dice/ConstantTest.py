import unittest
from Constant import Constant

class PositiveConstantTestCase(unittest.TestCase):
    def setUp(self):
        self.constant = Constant(6)

    def runTest(self):
        assert self.constant.roll().getResults() == [(6,True)], 'incorrect positive value'

class NegativeConstantTestCase(unittest.TestCase):
    def setUp(self):
        self.constant = Constant(-6)

    def runTest(self):
        assert self.constant.roll().getResults() == [(-6,True)], 'incorrect negative value'

def suite():
    suite = unittest.TestSuite()
    suite.addTest(PositiveConstantTestCase())
    suite.addTest(NegativeConstantTestCase())
    return suite
