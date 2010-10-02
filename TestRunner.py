import unittest
from Dice import TestRunner
import diceTest

def main():
    TestRunner.main()

    runner = unittest.TextTestRunner()
    runner.run(diceTest.suite())

if __name__ == '__main__':
    main()
