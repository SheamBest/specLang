from .calculator.interface import Calculator

def main():
    calc = Calculator()
    calc.userInterface()

if '__main__' == __name__:
    main()