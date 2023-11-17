from ASCII_art_generator.ascii_former import Art

def artFileSaver(filename, text):
    with open(filename, "w") as file:
        file.write(text)
    print(f"text  was saved into {filename}")

class ASCIIArtInterface:
    def __init__(self):
        self.art = Art()

    def setPrimaryData(self):
        text = input("Enter your text: ")
        self.art.setText(text)
        font = input("Choose art font (small, medium, big): ")
        self.art.setFont(font)
        
        symbol_to_replace = input(
            "Pick art symbol: ")
        self.art.setSymbolToReplace(symbol_to_replace)
        color = input("Choose art color: ")
        self.art.setColor(color)
        save_text = input("Do you want to save the text? (yes/no): ").lower()
        if save_text == "yes":
            self.saveToFile()

    def saveToFile(self):
        filename = input("Enter filename for saving art: ")
        artFileSaver(filename, self.art.generateASCIIArt())

    def launch(self):
        self.setPrimaryData()
        print(self.art.generateASCIIArt())
