from classes.operations.operations import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Exponentiation,
    SquareRoot,
    Modulus,
)
from classes.exceptions.math_exception import exception
from classes.history.history import History

# Головний клас калькулятора
class Calculator:
    """
    A simple calculator class that supports basic arithmetic operations,
    square root, modulus, and memory operations.

    This class provides an interactive user interface to perform calculations
    and maintains a history of performed operations.

    Attributes:
        decimal_places (int): The number of decimal places for the output.
        memory (float): A memory storage for calculator operations.
        history (History): An object to store the history of calculations.
    """
    def __init__(self):
        """
        Initializes the Calculator with default settings.
        """
        self.decimal_places = 2
        self.memory = 0
        self.history = History()

    # Відображення історії обчислень
    def display_history(self):
        """
        Displays the history of all calculations performed.
        """
        self.history.display()

    # Зміна кількості десяткових розрядів
    def change_decimal_places(self):
        """
        Prompts the user to change the number of decimal places for calculation results.
        """
        self.decimal_places = int(input("Введіть кількість десяткових розрядів: "))

    # Головний метод для виконання калькулятора
    def getUserChoice(self):
        """
        Prompts the user to enter their choice of operation.

        Returns:
            str: The user's choice of operation.
        """
        return input('Operation: [ +, -, *, /, ^, s, %, M ]: ')

    def getInputNumber(self, prompt):
        """
        Prompts the user for a number with a specific message.

        Args:
            prompt (str): The prompt message to display.

        Returns:
            float: The number entered by the user.
        """
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print('Please enter a valid number.')

    def getInputData(self):
        """
        Gets the user's choice of operation and the required numbers.

        Returns:
            tuple: The operation choice, first number, and second number (if applicable).
        """
        choice = self.getUserChoice()
        num1 = self.getInputNumber('Enter the first number: ')
        num2 = None
        if choice != 's' or 'M':
            num2 = self.getInputNumber('Enter the second number: ')
        return choice, num1, num2

    def performOperation(self, choice, num1, num2):
        """
        Performs the selected operation based on user input.

        Args:
            choice (str): The operation choice.
            num1 (float): The first number for the operation.
            num2 (float): The second number for the operation (if applicable).
        """
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
        elif operation == "M":
            self.memory = 0
            print(f"Значення {self.memory} збережено в пам'яті.")
        elif operation == "D":
            self.change_decimal_places()
        
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
        """
        Asks the user if they want to continue using the calculator.

        Returns:
            bool: True if the user wants to continue, False otherwise.
        """
        result = input('Do you want to continue? (y/n) ')
        return result == 'y'

    def userInterface(self):
        """
        The main user interface loop for the calculator.
        Handles user inputs, performs operations, and displays results.
        """
        while True:
            try:
                choice, num1, num2 = self.getInputData()
                self.performOperation(choice, num1, num2)
                print(f'Result: {self.result}')
                self.history.add_entry(f"{num1} {choice} {num2}", self.result)
            except Exception as e:
                print(f'Something went wrong: {e}. Please try again.')

            to_continue = self.askToContinue()
            if not to_continue:
                print('Good bye')
                break
            self.display_history()
    
    def run(self):
        """
        Runs the calculator's user interface.
        """
        self.userInterface()