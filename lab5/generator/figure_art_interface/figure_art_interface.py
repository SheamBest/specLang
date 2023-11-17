from abc import ABC, abstractmethod
from generator.figures.figure import Figure
from generator.figures.figures_3d.cube import Cube
from generator.figures.figures_2d.square import Square
from generator.colors.colors import textFileSaver


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Generate3DFigureCommand(Command):
    def __init__(self, figure_interface):
        self.figure_interface = figure_interface

    def execute(self):
        print(self.figure_interface.generate3dFigure())


class SetSizeCommand(Command):
    def __init__(self, figure_interface, new_size):
        self.figure_interface = figure_interface
        self.new_size = new_size

    def execute(self):
        self.figure_interface.setSize(self.new_size)


class SetColorCommand(Command):
    def __init__(self, figure_interface, new_color):
        self.figure_interface = figure_interface
        self.new_color = new_color

    def execute(self):
        self.figure_interface.setColor(self.new_color)

class FigureArtInterface(Figure):
    def __init__(self):
        super().__init__()
        self.type = "cube"
        self.left_padding = 5
        self.top_padding = 5
        self.bottom_padding = 5
        self.commands = {
            1: Generate3DFigureCommand(self),
            2: SetSizeCommand(self, 0),
            3: SetColorCommand(self, "")
        }

    def setType(self, type):
        self.type = type

    def setPaddings(self, left_padding, top_padding, bottom_padding):
        self.left_padding = left_padding
        self.top_padding = top_padding
        self.bottom_padding = bottom_padding

    def setPrimaryData(self):
        size = int(input("figure size: "))
        self.setSize(size)

        color = input(
            "figure color(blue, green, red, magenta, yellow, white, cyan): ")
        self.setColor(color)

        type = input("figure type(skip for default): ")
        if len(type):
            self.setType(type)

    def generateWithLeftPadding(self, text):
        lines = text.split('\n')
        padded_lines = [f"{' ' * self.left_padding}{line}" for line in lines]
        return '\n'.join(padded_lines)

    def generateWithTopPadding(self, text):
        space = self.top_padding * '\n'
        padded_lines = space + text
        return padded_lines

    def generateWithBottomPadding(self, text):
        space = self.bottom_padding * '\n'
        padded_lines = text + space
        return padded_lines

    def generateWithPaddings(self, text):
        return self.generateWithBottomPadding(self.generateWithTopPadding(self.generateWithLeftPadding(text)))

    def generate3dFigure(self):
        if self.type == 'cube':
            cube = Cube()
            cube.setSize(self.size)
            cube.setColor(self.color)
            return self.generateWithPaddings(cube.generateFigure())
        return super().generateFigure()

    def generate2dFigure(self):
        if self.type == 'cube':
            square = Square()
            square.setSize(self.size)
            square.setColor(self.color)
            return self.generateWithPaddings(square.generateFigure())
        return super().generateFigure()

    def saveToFile2d(self):
        filename = input("enter filename before saving: ")
        textFileSaver(
            filename, self.generate2dFigure())

    def saveToFile3d(self):
        filename = input("enter filename before saving: ")
        textFileSaver(
            filename, self.generate3dFigure())

    @staticmethod
    def show_menu():
        print("choose menu option")
        print("[ 1 ] - generate 3d figure")
        print("[ 2 ] - set size")
        print("[ 3 ] - set color(blue, green, red, magenta, yellow, white, cyan)")
        print("[ 4 ] - set type(cube)")
        print("[ 5 ] - set paddings")
        print("[ 6 ] - get 2d version of the figure")
        print("[ 7 ] - save to file(3d)")
        print("[ 8 ] - save to file(2d)")
        print("[ 0 ] - exit")

    def loopMenu(self):
        while True:
            self.show_menu()
            menu_choice = int(input("menu key: "))
            if (menu_choice == 1):
                print(self.generate3dFigure())
            elif (menu_choice == 2):
                new_size = int(input("enter new size: "))
                self.setSize(new_size)
            elif (menu_choice == 3):
                new_color = input("enter new color: ")
                self.setColor(new_color)
            elif (menu_choice == 4):
                new_type = input("enter new type: ")
                self.setType(new_type)
            elif (menu_choice == 5):
                left_padding = int(input("enter left padding: "))
                top_padding = int(input("enter top padding: "))
                bottom_padding = int(input("enter bottom padding: "))
                self.setPaddings(left_padding, top_padding, bottom_padding)
            elif (menu_choice == 6):
                print(self.generate2dFigure())
            elif (menu_choice == 7):
                self.saveToFile3d()
            elif (menu_choice == 8):
                self.saveToFile2d()
            else:
                break

    def launch(self):
        self.setPrimaryData()
        print(self.generate3dFigure())
        self.loopMenu()
