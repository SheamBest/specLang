import os
from termcolor import colored
import art

# Клас для генерації ASCII-арту
class AsciiArtGenerator:
    def __init__(self):
        self.text = ""
        self.font_name = ""
        self.color = "white"
        self.width = 80
        self.height = 20
        self.char = " "

    # Метод для отримання введення користувача з можливістю встановлення значення за замовчуванням
    def get_user_input(self, prompt, default=None):
        user_input = input(prompt).strip()
        return user_input if user_input else default

    # Метод для отримання ASCII-арту
    def get_art(self):
        try:
            return art.text2art(self.text, font=self.font_name)
        except Exception as e:
            print(f"Помилка: {e}")
            return art.text2art(self.text, font='block')

    # Метод для вибору кольору тексту
    def choose_color(self):
        colors = {
            'red': 'red',
            'blue': 'blue',
            'green': 'green'
        }
        color_name = input("Виберіть колір тексту (red/blue/green): ").lower()
        self.color = colors.get(color_name, 'white')

    # Метод для вибору розміру ASCII-арту
    def choose_size(self):
        try:
            self.width = int(input("Введіть ширину ASCII-арту: "))
            self.height = int(input("Введіть висоту ASCII-арту: "))
        except ValueError:
            self.width, self.height = 80, 20

    # Метод для генерації ASCII-арту
    def generate_ascii_art(self):
        self.text = self.get_user_input("Введіть слово або фразу для генерації ASCII-арту: ")
        self.font_name = self.get_user_input("Виберіть шрифт (стандартний/керований/блоки): ")

        art_object = self.get_art()

        self.choose_color()
        self.choose_size()

        self.char = input("Введіть символ, який ви хочете використовувати (наприклад, '@', '#', '*'): ")

        # Форматування та відображення ASCII-арту з кольором
        colored_art = colored(art_object, self.color)
        print("Попередній перегляд вашого ASCII-арту:")
        formatted_art = colored_art.center(self.width).replace(' ', self.char)
        print(formatted_art)

        # Опція для збереження ASCII-арту у файл
        save_option = input("Зберегти ASCII-арт у файл? (yes/no): ").lower()
        if save_option == 'yes':
            file_name = input("Введіть ім'я файлу для збереження: ")

            # Формування шляху до папки 'output', що знаходиться на рівень вище
            output_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'output')

            # Перевірка існування папки 'output' та її створення, якщо потрібно
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Формування повного шляху до файлу для збереження
            file_path = os.path.join(output_dir, file_name)

            # Збереження ASCII-арту у файл
            with open(file_path, 'w') as file:
                file.write(formatted_art)
                print(f"ASCII-арт був збережений у файлі '{file_path}'")

# Створення об'єкту класу і запуск генерації ASCII-арту
if __name__ == "__main__":
    generator = AsciiArtGenerator()
    generator.generate_ascii_art()
