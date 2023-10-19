import math

# Базовий клас для операцій
class Operation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Віртуальний метод для виконання операції
    def execute(self):
        pass

# Підкласи для конкретних операцій
class Addition(Operation):
    def execute(self):
        return self.num1 + self.num2

class Subtraction(Operation):
    def execute(self):
        return self.num1 - self.num2

class Multiplication(Operation):
    def execute(self):
        return self.num1 * self.num2

class Division(Operation):
    def execute(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return self.num1 / self.num2

class Exponentiation(Operation):
    def execute(self):
        return self.num1 ** self.num2

class SquareRoot(Operation):
    def execute(self):
        return math.sqrt(self.num1)

class Modulus(Operation):
    def execute(self):
        return self.num1 % self.num2
