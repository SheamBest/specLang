from ASCII_art_generator.generator.ascii_art import generate_custom_text, replaceSymbol, paintText


class ASCIIArt:
    def __init__(self):
        self.text = ""
        self.font = ""

    def setText(self, text):
        self.text = text

    def setFont(self, font):
        self.font = font

    def generateArt(self):
        return generate_custom_text(input_string=self.text, font_name=self.font)
    
class Art(ASCIIArt):
    def __init__(self):
        super().__init__()
        self.symbol_to_replace = ""
        self.color = ""

    def setSymbolToReplace(self, symbol_to_replace):
        self.symbol_to_replace = symbol_to_replace

    def setColor(self, color):
        self.color = color

    def generateASCIIArt(self):
        generated_art = self.generateArt()
        text_art_replaced = replaceSymbol(
            generated_art, self.symbol_to_replace)
        text_art_painted = paintText(
            text_art_replaced, self.color)
        return text_art_painted