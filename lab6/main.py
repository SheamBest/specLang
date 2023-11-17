import unittest
from calculator.interface import Calculator
from calculator.tests.test import CalculatorTest


def main():
    test_calculator = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    test_loader = unittest.TextTestRunner()

    test_loader.run(test_calculator)
    input()

if '__main__' == __name__:
    main()
    calc = Calculator()
    calc.userInterface()