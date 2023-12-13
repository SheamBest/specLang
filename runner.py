"""
This module implements a console menu for launching various programs.
It utilizes ConsoleMenu to create a user interface.
"""

import logging
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from classes.facade.facade import LabRunnerFacade

class Runner(LabRunnerFacade):
    def __init__(self):
        """
        Initializes the Runner instance.
        
        Sets up the logging configuration and initializes the LabRunnerFacade.
        """
        super().__init__()
        logging.basicConfig(filename='logs/example.log', level=logging.DEBUG)

    def log_info_run(self, run):
        """
        Logs information about the program being run.

        Args:
            run (str): Description of the program being run.
        """
        logging.info('Starting: %s', run)

    def log_error_run(self, run):
        """
        Logs uncaught errors that occur during program execution.

        Args:
            run (str): Description of the program where the error occurred.
        """
        logging.error('Failed to execute: %s', run)

def main():
    """
    Main function to initialize and display the console menu.
    
    It initializes the console menu with a title 'Runner', sets up the Runner object,
    and adds various menu items that trigger methods of the Runner object. In case of any
    exceptions, it logs the error.
    """
    try:
        runner = Runner()
        menu = ConsoleMenu("Runner")
        runner.log_info_run("ConsoleMenu initialized")

        runner.log_info_run("Runner initialized")

        menu.append_item(FunctionItem("Calculator", runner.run_calculator))
        menu.append_item(FunctionItem("OOP Calculator", runner.run_oop_calculator))
        menu.append_item(FunctionItem("ASCII Art", runner.run_ascii_art))
        menu.append_item(FunctionItem("2D ASCII Art without additional libraries", runner.run_2d_ascii_art))
        menu.append_item(FunctionItem("3D ASCII Arts", runner.run_3d_ascii_art))
        menu.append_item(FunctionItem("Calculator (Lab6)", runner.run_calculator_lab6))
        menu.append_item(FunctionItem("Calculator tests", runner.run_calculator_tests))
        menu.append_item(FunctionItem("API requests", runner.run_api_requests))
        menu.append_item(FunctionItem("API requests tests", runner.run_api_requests_tests))
        menu.append_item(FunctionItem("Data analysis", runner.run_data_analysis))

        menu.show()
        runner.log_info_run("Menu displayed")
    except Exception as e:
        runner.log_error_run(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
