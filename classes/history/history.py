class History:
    """
    A class for storing the history of calculations.

    This class provides functionality to add new entries to the history 
    and display all recorded calculations.

    Attributes:
        entries (list of dict): A list to store the history of calculations.
                                Each entry is a dictionary with 'expression' and 'result'.
    """

    def __init__(self):
        """
        Initializes the History instance with an empty list of entries.
        """
        self.entries = []

    def add_entry(self, expression, result):
        """
        Adds a new entry to the history.

        Args:
            expression (str): The expression or operation that was calculated.
            result (float): The result of the calculation.
        """
        self.entries.append({'expression': expression, 'result': result})

    def display(self):
        """
        Displays the entire history of calculations.

        Iterates through the list of entries and prints each calculation and its result.
        If the history is empty, no output is generated.
        """
        if self.entries:
            print("Operation history:")
            for i, entry in enumerate(self.entries, 1):
                print(f"{i}. Operation: {entry['expression']}, Result: {entry['result']}")
