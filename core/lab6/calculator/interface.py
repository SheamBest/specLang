# Імпортуємо необхідні класи операцій та винятків.
from .operations.operations import Addition, Subtraction, Multiplication, Division, Exponentiation, SquareRoot, Modulus
from .exceptions.exceptions import exception

# Клас Calculator для виконання арифметичних операцій.
class Calculator:
    def __init__(self):
        self.result = 0.0

    # Отримання вибору операції від користувача.
    def getUserChoice(self):
        return input('Operation: [ +, -, *, /, ^, s, % ]: ')

    # Отримання числа від користувача з обраним повідомленням-запитом.
    def getInputNumber(self, prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print('Please enter a valid number.')

    # Отримання даних для виконання операції від користувача.
    def getInputData(self):
        choice = self.getUserChoice()
        num1 = self.getInputNumber('Enter the first number: ')
        num2 = None
        if choice not in ('√'):
            num2 = self.getInputNumber('Enter the second number: ')
        return choice, num1, num2

    # Виконання обраної операції з використанням введених чисел.
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

    # Питання користувача, чи бажає він продовжувати роботу з калькулятором.
    @staticmethod
    def askToContinue():
        result = input('Do you want to continue? (y/n) ')
        return result == 'y'

    # Головний інтерфейс користувача для взаємодії з калькулятором.
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
