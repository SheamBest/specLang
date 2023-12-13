import math

class Operation:
    """
    Base class for arithmetic operations.

    This class is designed to be subclassed for specific arithmetic operations.
    It ensures input validation and provides a template method 'execute'.

    Attributes:
        num1 (int or float): The first operand for the operation.
        num2 (int or float): The second operand for the operation.
    """

    def __init__(self, num1, num2):
        """
        Initializes the Operation with two numbers, validating their types.

        Args:
            num1 (int or float): The first number.
            num2 (int or float): The second number.
        """
        InputValidator(num1)
        InputValidator(num2)
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        """
        Virtual method for executing the operation.

        To be implemented by subclasses.

        Returns:
            The result of the arithmetic operation.
        """
        pass

class InputValidator:
    """
    Class for validating input values for arithmetic operations.

    Raises a TypeError if the input is not a number.
    """

    def __init__(self, num):
        """
        Initializes the InputValidator and checks the input.

        Args:
            num (int or float): The number to validate.

        Raises:
            TypeError: If 'num' is not an integer or float.
        """
        if not isinstance(num, (int, float)):
            raise TypeError("Invalid number format for input.")

# Subclasses for specific operations
class Addition(Operation):
    """
    Class for addition operation.
    """

    def execute(self):
        """
        Executes the addition operation.

        Returns:
            float: The result of adding num1 and num2.
        """
        return self.num1 + self.num2

class Subtraction(Operation):
    """
    Class for subtraction operation.
    """

    def execute(self):
        """
        Executes the subtraction operation.

        Returns:
            float: The result of subtracting num2 from num1.
        """
        return self.num1 - self.num2

class Multiplication(Operation):
    """
    Class for multiplication operation.
    """

    def execute(self):
        """
        Executes the multiplication operation.

        Returns:
            float: The result of multiplying num1 by num2.
        """
        return self.num1 * self.num2

class Division(Operation):
    """
    Class for division operation.
    """

    def execute(self):
        """
        Executes the division operation.

        Returns:
            float: The result of dividing num1 by num2.

        Raises:
            ValueError: If trying to divide by zero.
        """
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return self.num1 / self.num2

class Exponentiation(Operation):
    """
    Class for exponentiation operation.
    """

    def execute(self):
        """
        Executes the exponentiation operation.

        Returns:
            float: The result of raising num1 to the power of num2.
        """
        return self.num1 ** self.num2

class SquareRoot(Operation):
    """
    Class for square root operation.
    """

    def execute(self):
        """
        Executes the square root operation.

        Returns:
            float: The square root of num1.
        """
        return math.sqrt(self.num1)

class Modulus(Operation):
    """
    Class for modulus operation.
    """

    def execute(self):
        """
        Executes the modulus operation.

        Returns:
            float: The result of num1 modulus num2.
        """
        return self.num1 % self.num2
