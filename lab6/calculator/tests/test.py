import unittest
from calculator.operations.operations import Addition, Division, Multiplication, Subtraction
from calculator.exceptions.exceptions import exception


class CalculatorTest(unittest.TestCase):
    # addition
    def testAdditionPositiveNumbers(self):
        addition_operation = Addition(5, 3)

        self.assertEqual(addition_operation.execute(), 8)

    def testAdditionNegativeNumbers(self):
        addition_operation = Addition(-2, -4)

        self.assertEqual(addition_operation.execute(), -6)

    def testAdditionMixedNumbers(self):
        addition_operation = Addition(4, -1)

        self.assertEqual(addition_operation.execute(), 3)

    # substraction
    def testSubtractionPositiveNumbers(self):
        subtraction_operation = Subtraction(5, 3)

        self.assertEqual(subtraction_operation.execute(), 2)

    def testSubtractionNegativeNumbers(self):
        subtraction_operation = Subtraction(-2, -4)

        self.assertEqual(subtraction_operation.execute(), 2)

    def testSubtractionMixedNumbers(self):
        subtraction_operation = Subtraction(4, -1)

        self.assertEqual(subtraction_operation.execute(), 5)

    def testSubtractionZero(self):
        subtraction_operation = Subtraction(5, 5)

        self.assertEqual(subtraction_operation.execute(), 0)

    def testSubtractionNegativeResult(self):
        subtraction_operation = Subtraction(10, 15)

        self.assertEqual(subtraction_operation.execute(), -5)

    # multiplication
    def testMultiplicationPositiveNumbers(self):
        multiplication_operation = Multiplication(5, 3)

        self.assertEqual(multiplication_operation.execute(), 15)

    def testMultiplicationNegativeNumbers(self):
        multiplication_operation = Multiplication(-2, -4)

        self.assertEqual(multiplication_operation.execute(), 8)

    def testMultiplicationMixedNumbers(self):
        multiplication_operation = Multiplication(4, -1)

        self.assertEqual(multiplication_operation.execute(), -4)

    def testMultiplicationZero(self):
        multiplication_operation = Multiplication(5, 0)

        self.assertEqual(multiplication_operation.execute(), 0)

    def testMultiplicationByZero(self):
        multiplication_operation = Multiplication(0, 5)

        self.assertEqual(multiplication_operation.execute(), 0)

    # division
    def testDivisionPositiveDecimalNumbers(self):
        division_operation = Division(10.5, 2.5)

        self.assertEqual(division_operation.execute(), 4.2)

    def testDivisionNegativeDecimalNumbers(self):
        division_operation = Division(-10.5, -2.5)

        self.assertEqual(division_operation.execute(), 4.2)

    def testDivisionMixedDecimalNumbers(self):
        division_operation = Division(4.5, -2)

        self.assertEqual(division_operation.execute(), -2.25)

    def testDivisionByZero(self):
        with self.assertRaises(ValueError):
            Division(10.5, 0).execute()

    # error handling
    def testDivisionByZeroError(self):
        with self.assertRaises(ValueError):
            exception(Division(10, 0).execute())

    def testInvalidOperationError(self):
        with self.assertRaises(TypeError):
            exception(Division('abc', 0).execute())

    def testInvalidNumberError(self):
        with self.assertRaises(TypeError):
            exception(Division(10, 'abc').execute())

    def testCalculator(self):
        self.testAdditionPositiveNumbers()
        self.testAdditionNegativeNumbers()
        self.testAdditionMixedNumbers()

        self.testSubtractionPositiveNumbers()
        self.testSubtractionNegativeNumbers()
        self.testSubtractionMixedNumbers()
        self.testSubtractionZero()
        self.testSubtractionNegativeResult()

        self.testMultiplicationPositiveNumbers()
        self.testMultiplicationNegativeNumbers()
        self.testMultiplicationMixedNumbers()
        self.testMultiplicationZero()
        self.testMultiplicationByZero()

        self.testDivisionPositiveDecimalNumbers()
        self.testDivisionNegativeDecimalNumbers()
        self.testDivisionMixedDecimalNumbers()
        self.testDivisionByZero()

        self.testDivisionByZeroError()
        self.testInvalidOperationError()
        self.testInvalidNumberError()
