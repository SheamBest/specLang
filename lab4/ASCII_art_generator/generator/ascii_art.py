from ASCII_art_generator.generator.letters.letters import fonts
import re
from termcolor import colored

def generate_custom_text(input_string, font_name):
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
    max_lines = max(len(font_map['a'].strip().split('\n')),
                    len(font_map['b'].strip().split('\n')),
                    len(font_map['c'].strip().split('\n')))
    return max_lines

# Function to generate the result array
def generateResultArray(lines, max_lines, font_map):
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
    default_art = font_map['a'].strip().split('\n')
    for i in range(max_lines):
        line_array[i] += " " * len(default_art[0]) + " "
    return line_array

# Function to format the result array as a string
def formatResult(result_array):
    result_string = "\n".join(result_array).replace('_', ' ')
    return result_string

# Function to replace a symbol
def replaceSymbol(text, symbol_to_replace):
    if (len(symbol_to_replace)):
        pattern = r'\S'
        replaced = re.sub(pattern, symbol_to_replace, text)
        return replaced
    else:
        return text

# Function to paint colored text
def paintText(text, color):
    if (len(color)):
        painted = colored(text, color)
        return painted
    else:
        return text