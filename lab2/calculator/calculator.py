from calculator.operation.operation import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Exponentiation,
    SquareRoot,
    Modulus,
)
from calculator.operation.history import History

# Головний клас калькулятора
class Calculator:
    def __init__(self):
        self.decimal_places = 2
        self.memory = 0
        self.history = History()

    # Відображення історії обчислень
    def display_history(self):
        self.history.display()

    # Зміна кількості десяткових розрядів
    def change_decimal_places(self):
        self.decimal_places = int(input("Введіть кількість десяткових розрядів: "))

    # Головний метод для виконання калькулятора
    def run(self):
        while True:
            try:
                self.display_history()

                num1 = float(input("Введіть перше число: "))
                num2 = float(input("Введіть друге число: "))

                operator = input("Введіть оператор (+, -, *, /, ^, √, %, M - для збереження в пам'ять, D - для зміни десяткових розрядів): ")

                if operator in ('+', '-', '*', '/', '^', '√', '%'):
                    # Створення об'єкту відповідно до вибраної операції
                    operation = self.create_operation(num1, num2, operator)
                    result = operation.execute()
                elif operator == "M":
                    self.memory = 0
                    print(f"Значення {self.memory} збережено в пам'яті.")
                elif operator == "D":
                    self.change_decimal_places()
                    continue
                else:
                    print("Помилка! Введіть дійсний оператор (+, -, *, /, ^, √, %, M, D).")
                    continue

                formatted_result = round(result, self.decimal_places)
                print(f"Результат обчислення: {formatted_result}")

                self.history.add_entry(f"{num1} {operator} {num2}", formatted_result)

            except ValueError:
                print("Помилка! Введено недійсне число.")
            except ZeroDivisionError as e:
                print(f"Помилка: {e}")

            repeat = input("Виконати ще одне обчислення? (Так/Ні): ").lower()
            if repeat != "так":
                break

        self.display_history()

    # Метод для створення об'єкту операції залежно від вибору користувача
    def create_operation(self, num1, num2, operator):
        operations = {
            '+': Addition(num1, num2),
            '-': Subtraction(num1, num2),
            '*': Multiplication(num1, num2),
            '/': Division(num1, num2),
            '^': Exponentiation(num1, num2),
            '√': SquareRoot(num1, num2),
            '%': Modulus(num1, num2),
        }
        return operations.get(operator, None)
