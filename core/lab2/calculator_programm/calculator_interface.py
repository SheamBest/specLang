# Імпортуємо необхідні класи з інших модулів
from .operation.operation import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Exponentiation,
    SquareRoot,
    Modulus,
)
from .exception.exception import exception
from .history.history import History

# Головний клас калькулятора
class Calculator:
    def __init__(self):
        # Ініціалізуємо початкові значення
        self.decimal_places = 2  # Кількість десяткових розрядів за замовчуванням
        self.memory = 0  # Пам'ять калькулятора (для збереження результатів)
        self.history = History()  # Об'єкт для ведення історії операцій

    # Метод для відображення історії обчислень
    def display_history(self):
        self.history.display()

    # Метод для зміни кількості десяткових розрядів
    def change_decimal_places(self):
        self.decimal_places = int(input("Введіть кількість десяткових розрядів: "))

    # Метод для отримання вибору користувача щодо операції
    def getUserChoice(self):
        return input('Операція: [ +, -, *, /, ^, s, %, M ]: ')

    # Метод для отримання введеного числа від користувача
    def getInputNumber(self, prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print('Будь ласка, введіть коректне число.')

    # Метод для отримання введених даних від користувача (операція та числа)
    def getInputData(self):
        choice = self.getUserChoice()
        num1 = self.getInputNumber('Введіть перше число: ')
        num2 = None
        if choice != 's' or 'M':
            num2 = self.getInputNumber('Введіть друге число: ')
        return choice, num1, num2

    # Метод для виконання операції на числах
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
        elif choice == "M":
            self.memory = 0
            print(f"Значення {self.memory} збережено в пам'яті.")
        elif choice == "D":
            self.change_decimal_places()
        
        if operation:
            try:
                self.result = operation.execute()
            except Exception as e:
                self.result = exception(e)
        else:
            self.result = exception(ValueError(
                'Невірний вибір. Спробуйте ще раз.'))

    # Метод для запиту користувача, чи бажає він продовжити використання калькулятора
    @staticmethod
    def askToContinue():
        result = input('Бажаєте продовжити? (так/ні) ')
        return result == 'так'

    # Метод, який реалізує користувацький інтерфейс калькулятора
    def userInterface(self):
        while True:
            try:
                choice, num1, num2 = self.getInputData()
                self.performOperation(choice, num1, num2)
                print(f'Результат: {self.result}')
                self.history.add_entry(f"{num1} {choice} {num2}", self.result)
            except Exception as e:
                print(f'Щось пішло не так: {e}. Будь ласка, спробуйте ще раз.')

            to_continue = self.askToContinue()
            if not to_continue:
                print('До побачення')
                break
            self.display_history()

    # Метод для запуску калькулятора
    def run(self):
        self.userInterface()
