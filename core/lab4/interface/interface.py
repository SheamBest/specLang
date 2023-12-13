# Імпортуємо необхідні модулі
from ..ASCII_art_generator.ascii_former import Art
import os

# Функція для збереження тексту в файл
def artFileSaver(filename, text):
    with open(filename, "w") as file:
        file.write(text)
    print(f"Текст був збережений у файл {filename}")

# Клас для взаємодії з генератором ASCII-арту
class ASCIIArtInterface:
    def __init__(self):
        self.art = Art()

    # Метод для встановлення основних параметрів ASCII-арту
    def setPrimaryData(self):
        text = input("Введіть текст: ")
        self.art.setText(text)
        font = input("Виберіть шрифт для арту (small, medium, big): ")
        self.art.setFont(font)
        
        symbol_to_replace = input("Виберіть символ для арту: ")
        self.art.setSymbolToReplace(symbol_to_replace)
        color = input("Виберіть колір для арту: ")
        self.art.setColor(color)
        save_text = input("Бажаєте зберегти текст? (так/ні): ").lower()
        if save_text == "так":
            self.saveToFile()

    # Метод для збереження ASCII-арту в файл
    def saveToFile(self):
        filename = input("Введіть ім'я файлу для збереження арту: ")

        # Отримуємо шлях до поточного файлу
        current_file_path = os.path.dirname(__file__)

        # Формуємо шлях до папки 'output', яка знаходиться на два рівні вище
        output_dir = os.path.join(current_file_path, '..', '..', '..', 'output')

        # Перевіряємо, чи існує папка 'output', і створюємо її, якщо потрібно
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Повний шлях до файлу для збереження
        file_path = os.path.join(output_dir, filename)

        # Викликаємо функцію для збереження арт-файлу
        artFileSaver(file_path, self.art.generateASCIIArt())

    # Метод для запуску інтерфейсу
    def launch(self):
        self.setPrimaryData()
        print(self.art.generateASCIIArt())
