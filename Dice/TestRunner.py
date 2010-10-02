import ConstantTest
import RollResultTest
import unittest

def main():
    runner = unittest.TextTestRunner()
    runner.run(ConstantTest.suite())
    runner.run(RollResultTest.suite())

if __name__ == '__main__':
    main()
