from calculator.operations.operations import Addition, Subtraction, Multiplication, Division, Exponentiation, SquareRoot, Modulus
from calculator.exceptions.exceptions import exception


class Calculator:
    def __init__(self):
        self.result = 0.0

    def getUserChoice(self):
        return input('Operation: [ +, -, *, /, ^, s, % ]: ')

    def getInputNumber(self, prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print('Please enter a valid number.')

    def getInputData(self):
        choice = self.getUserChoice()
        num1 = self.getInputNumber('Enter the first number: ')
        num2 = None
        if choice not in ('√'):
            num2 = self.getInputNumber('Enter the second number: ')
        return choice, num1, num2

    def performOperation(self, choice, num1, num2):
        operation = None

        if choice == '+':
            operation = Addition(num1, num2)
        elif choice == '-':
            operation = Subtraction(num1, num2)
        elif choice == '*':
            operation = Multiplication(num1, num2)
        elif choice == '/':
            operation = Division(num1, num2)
        elif choice == '^':
            operation = Exponentiation(num1, num2)
        elif choice == 's':
            operation = SquareRoot(num1, None)
        elif choice == '%':
            operation = Modulus(num1, num2)

        if operation:
            try:
                self.result = operation.execute()
            except Exception as e:
                self.result = exception(e)
        else:
            self.result = exception(ValueError(
                'Invalid choice. Please try again.'))

    @staticmethod
    def askToContinue():
        result = input('Do you want to continue? (y/n) ')
        return result == 'y'

    def userInterface(self):
        while True:
            try:
                choice, num1, num2 = self.getInputData()
                self.performOperation(choice, num1, num2)
                print(f'Result: {self.result}')
            except Exception as e:
                print(f'Something went wrong: {e}. Please try again.')

            to_continue = self.askToContinue()
            if not to_continue:
                print('Good bye')
                break
