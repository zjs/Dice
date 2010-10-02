import unittest
from dice import _parse_string, _string_to_strings, _string_to_sets
from Dice import DiceSet

class ParseStringTestCase(unittest.TestCase):
    def testAdB(self):
        assert _parse_string("1d6") == {'count':1,'sides':6,'keep':1,'number':1}
        assert _parse_string("2d6") == {'count':2,'sides':6,'keep':2,'number':1}
        assert _parse_string("3d7") == {'count':3,'sides':7,'keep':3,'number':1}

    def testAdBkC(self):
        assert _parse_string("1d6k1") == {'count':1,'sides':6,'keep':1,'number':1}
        assert _parse_string("3d7k2") == {'count':3,'sides':7,'keep':2,'number':1}
 
    def testAdBxC(self):
        assert _parse_string("1d6x1") == {'count':1,'sides':6,'keep':1,'number':1}
        assert _parse_string("3d7x4") == {'count':3,'sides':7,'keep':3,'number':4}

    def testAdBkCxD(self):
        assert _parse_string("1d6k1x1") == {'count':1,'sides':6,'keep':1,'number':1}
        assert _parse_string("3d7k2x4") == {'count':3,'sides':7,'keep':2,'number':4}

    def testConstant(self):
        assert _parse_string("6") == {'count':6,'sides':1,'keep':6,'number':1}

    def testNegativeConstant(self):
        assert _parse_string("-6") == {'count':6,'sides':-1,'keep':6,'number':1}

class SplitStringTestCase(unittest.TestCase):
    def testOne(self):
        assert _string_to_strings("6") == ["6"]
        assert _string_to_strings("-6") == ["-6"]
        assert _string_to_strings("1d6") == ["1d6"]
        assert _string_to_strings("2d6k1") == ["2d6k1"]
        assert _string_to_strings("2d6k1x3") == ["2d6k1x3"]

    def testTwo(self):
        assert _string_to_strings("1d6+5") == ["1d6","5"]
        assert _string_to_strings("1d6-5") == ["1d6","-5"]

    def testThree(self):
        assert _string_to_strings("2d6k1+1d6+5") == ["2d6k1","1d6","5"]
        assert _string_to_strings("2d6k1+1d6-5") == ["2d6k1","1d6","-5"]
        assert _string_to_strings("2d6k1x3+1d6+5") == ["2d6k1x3","1d6","5"]

class StringToSetsTestCase(unittest.TestCase):
    def testConstant(self):
        assert _string_to_sets("6") == [DiceSet(6,1)]

    def testSimple(self):
        assert _string_to_sets("1d6") == [DiceSet(1,6)]

    def testX(self):
        assert _string_to_sets("1d6x3") == [DiceSet(1,6), DiceSet(1,6), DiceSet(1,6)]

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ParseStringTestCase, 'test'))
    suite.addTest(unittest.makeSuite(SplitStringTestCase, 'test'))
    #suite.addTest(unittest.makeSuite(StringToSetsTestCase, 'test')) #Need to come up with a better way to test
    return suite
