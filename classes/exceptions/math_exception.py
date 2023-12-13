class CalculatorError:
    """
    Custom exception class for calculator errors.

    Attributes:
        error_type (type): The type of the exception.
        message (str): The error message.

    Methods:
        __str__: Returns a string representation of the error.
    """

    def __init__(self, error_type, message):
        """
        Initializes a CalculatorError instance with the given error type and message.

        Args:
            error_type (type): The type of the exception.
            message (str): The descriptive message for the exception.
        """
        self.error_type = error_type
        self.message = message

    def __str__(self):
        """
        Returns the string representation of the CalculatorError.

        Combines the error type and message into a formatted string.

        Returns:
            str: A formatted error message.
        """
        return f'{self.error_type}: {self.message}'


def exception(exception):
    """
    Helper function to create a CalculatorError instance from an exception.

    Args:
        exception (Exception): The exception to convert into a CalculatorError.

    Returns:
        CalculatorError: A CalculatorError instance encapsulating the given exception.
    """
    return CalculatorError(type(exception), exception.__str__())
