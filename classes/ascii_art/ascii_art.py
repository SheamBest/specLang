from classes.ascii_art.letters import fonts
import re
from termcolor import colored

def generate_custom_text(input_string, font_name):
    """
    Generate custom ASCII art text using a specified font.

    Args:
        input_string (str): The string to convert into ASCII art.
        font_name (str): The name of the font to use for ASCII art generation.

    Returns:
        str: The generated ASCII art as a string.
    """
    # Retrieve font map
    font_map = fonts(font_name)

    # Split the input string into lines
    lines = input_string.split('\n')

    # Determine the maximum number of lines in a character in the font
    max_lines = determineMaxLines(font_map)

    # Generate the custom text
    result_array = generateResultArray(lines, max_lines, font_map)

    # Format the result as a string
    result_string = formatResult(result_array)

    return result_string

# Function to determine the maximum number of lines in a character in the font
def determineMaxLines(font_map):
    """
    Determine the maximum number of lines in a character in the font map.

    Args:
        font_map (dict): A dictionary containing font characters and their ASCII art representations.

    Returns:
        int: The maximum number of lines in a character in the font.
    """
    max_lines = max(len(font_map['a'].strip().split('\n')),
                    len(font_map['b'].strip().split('\n')),
                    len(font_map['c'].strip().split('\n')))
    return max_lines

# Function to generate the result array
def generateResultArray(lines, max_lines, font_map):
    """
    Generate the result array for ASCII art based on input lines, maximum line count, and font map.

    Args:
        lines (list): List of lines to be converted into ASCII art.
        max_lines (int): The maximum number of lines in a character in the font.
        font_map (dict): A dictionary containing font characters and their ASCII art representations.

    Returns:
        list: An array representing the ASCII art.
    """
    result_array = []
    for line in lines:
        line_array = [""] * max_lines
        for char in line:
            if char.lower() in font_map:
                line_array = addCharacterToLineArray(
                    char, line_array, max_lines, font_map)
            else:
                line_array = addDefaultCharacterToLineArray(
                    line_array, max_lines, font_map)
        result_array.extend(line_array)
    return result_array

# Function to add a character to the line array
def addCharacterToLineArray(char, line_array, max_lines, font_map):
    """
    Add a character to the line array, expanding it into ASCII art.

    Args:
        char (str): The character to add.
        line_array (list): The current line array being constructed.
        max_lines (int): The maximum number of lines in a character in the font.
        font_map (dict): A dictionary containing font characters and their ASCII art representations.

    Returns:
        list: The updated line array with the added character.
    """
    for i in range(max_lines):
        art = font_map[char.lower()].strip().split('\n')
        if i < len(art):
            diff = len(font_map['a'].strip().split('\n')[0]) - len(art[i])
            line_array[i] += art[i] + " " * diff + " "
        else:
            default_art = font_map['a'].strip().split('\n')
            line_array[i] += " " * len(default_art[0]) + " "
    return line_array

# Function to add a default character to the line array
def addDefaultCharacterToLineArray(line_array, max_lines, font_map):
    """
    Add a default space character to the line array.

    Args:
        line_array (list): The current line array being constructed.
        max_lines (int): The maximum number of lines in a character in the font.
        font_map (dict): A dictionary containing font characters and their ASCII art representations.

    Returns:
        list: The updated line array with the added default character.
    """
    default_art = font_map['a'].strip().split('\n')
    for i in range(max_lines):
        line_array[i] += " " * len(default_art[0]) + " "
    return line_array

# Function to format the result array as a string
def formatResult(result_array):
    """
    Format the result array as a string.

    Args:
        result_array (list): An array representing the ASCII art.

    Returns:
        str: The formatted ASCII art as a string.
    """
    result_string = "\n".join(result_array).replace('_', ' ')
    return result_string

# Function to replace a symbol
def replaceSymbol(text, symbol_to_replace):
    """
    Replace all non-space characters in the text with a specified symbol.

    Args:
        text (str): The ASCII art text.
        symbol_to_replace (str): The symbol to replace all non-space characters with.

    Returns:
        str: The text with symbols replaced.
    """
    if (len(symbol_to_replace)):
        pattern = r'\S'
        replaced = re.sub(pattern, symbol_to_replace, text)
        return replaced
    else:
        return text

# Function to paint colored text
def paintText(text, color):
    """
    Apply a color to the ASCII art text using the termcolor library.

    Args:
        text (str): The ASCII art text.
        color (str): The color to apply.

    Returns:
        str: The colored ASCII art text.
    """
    if (len(color)):
        painted = colored(text, color)
        return painted
    else:
        return text

class ASCIIArt:
    def __init__(self):
        """
        Initialize an ASCIIArt object with default text and font attributes.
        """
        self.text = ""
        self.font = ""

    def setText(self, text):
        """
        Set the text to be converted into ASCII art.

        Args:
            text (str): The text to be converted.
        """
        self.text = text

    def setFont(self, font):
        """
        Set the font for the ASCII art.

        Args:
            font (str): The name of the font to be used.
        """
        self.font = font

    def generateArt(self):
        """
        Generate ASCII art based on the set text and font.

        Returns:
            str: The generated ASCII art.
        """
        return generate_custom_text(input_string=self.text, font_name=self.font)
    
class Art(ASCIIArt):
    def __init__(self):
        """
        Initialize an Art object, extending ASCIIArt with additional attributes 
        for symbol replacement and coloring.
        """
        super().__init__()
        self.symbol_to_replace = ""
        self.color = ""

    def setSymbolToReplace(self, symbol_to_replace):
        """
        Set the symbol in the ASCII art that will be replaced.

        Args:
            symbol_to_replace (str): The symbol to be replaced in the ASCII art.
        """
        self.symbol_to_replace = symbol_to_replace

    def setColor(self, color):
        """
        Set the color for the ASCII art.

        Args:
            color (str): The color to be applied to the ASCII art.
        """
        self.color = color

    def generateASCIIArt(self):
        """
        Generate colored ASCII art with specified symbols replaced.

        Returns:
            str: The final colored ASCII art with specified symbols replaced.
        """
        generated_art = self.generateArt()
        text_art_replaced = replaceSymbol(
            generated_art, self.symbol_to_replace)
        text_art_painted = paintText(
            text_art_replaced, self.color)
        return text_art_painted
