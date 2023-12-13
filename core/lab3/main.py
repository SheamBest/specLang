from .art_generator.art_gen import AsciiArtGenerator

def main():
    ascii_art_generator = AsciiArtGenerator()
    ascii_art_generator.generate_ascii_art()

if __name__ == "__main__":
    main()
    input()
