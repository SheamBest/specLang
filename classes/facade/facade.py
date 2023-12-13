class LabRunnerFacade:
    """
    A facade class for running various laboratory applications. 

    This class acts as a central point for executing different lab tasks, 
    encapsulating the complexity of individual lab module executions. 
    It imports and manages several lab modules, each representing a different
    task such as calculators, ASCII art creators, and data analysis tools.

    Attributes:
        lab1 (module): Module for running the basic calculator from lab1.
        lab2 (module): Module for running the OOP calculator from lab2.
        lab3 (module): Module for running the ASCII art generator from lab3.
        lab4 (module): Module for running the 2D ASCII art generator from lab4.
        lab5 (module): Module for running the 3D ASCII art generator from lab5.
        lab6 (module): Module for running the calculator from lab6.
        lab6_unittests (module): Module for running unit tests for lab6 calculator.
        lab7 (module): Module for running API requests from lab7.
        lab7_unittests (module): Module for running unit tests for lab7 API requests.
        lab8 (module): Module for running data analysis from lab8.
    """

    def __init__(self):
        """
        Initializes the LabRunnerFacade instance.

        Sets up logging and imports necessary lab modules, storing their references
        for later use. Each lab module is accessible as an attribute of the instance.
        """
        # Import modules here
        import core.lab1.main
        import core.lab2.main
        import core.lab3.main
        import core.lab4.main
        import core.lab5.main
        import core.lab6.main
        import core.lab6.unit_test
        import core.lab7.main
        import core.lab7.unittests
        import core.lab8.main

        # Store module references in the facade
        self.lab1 = core.lab1.main
        self.lab2 = core.lab2.main
        self.lab3 = core.lab3.main
        self.lab4 = core.lab4.main
        self.lab5 = core.lab5.main
        self.lab6 = core.lab6.main
        self.lab6_unittests = core.lab6.unit_test
        self.lab7 = core.lab7.main
        self.lab7_unittests = core.lab7.unittests
        self.lab8 = core.lab8.main

    def run_calculator(self):
        """
        Runs the basic calculator application from lab1.
        """
        self.lab1.main()

    def run_oop_calculator(self):
        """
        Runs the Object-Oriented Programming (OOP) calculator from lab2.
        """
        self.lab2.main()

    def run_ascii_art(self):
        """
        Executes the ASCII art generator from lab3.
        """
        self.lab3.main()

    def run_2d_ascii_art(self):
        """
        Executes the 2D ASCII art generator from lab4.
        """
        self.lab4.main()

    def run_3d_ascii_art(self):
        """
        Executes the 3D ASCII art generator from lab5.
        """
        self.lab5.main()

    def run_calculator_lab6(self):
        """
        Runs the advanced calculator application from lab6.
        """
        self.lab6.main()

    def run_calculator_tests(self):
        """
        Executes the unit tests for the calculator application from lab6.
        """
        self.lab6_unittests.main()

    def run_api_requests(self):
        """
        Executes the API requests application from lab7.
        """
        self.lab7.main()

    def run_api_requests_tests(self):
        """
        Executes the unit tests for the API requests application from lab7.
        """
        self.lab7_unittests.main()

    def run_data_analysis(self):
        """
        Runs the data analysis application from lab8.
        """
        self.lab8.main()
