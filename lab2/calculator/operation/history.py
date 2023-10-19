# Клас для збереження історії обчислень
class History:
    def __init__(self):
        self.entries = []

    # Додавання запису в історію
    def add_entry(self, expression, result):
        self.entries.append({'expression': expression, 'result': result})

    # Відображення історії
    def display(self):
        if self.entries:
            print("Історія обчислень:")
            for i, entry in enumerate(self.entries, 1):
                print(f"{i}. Вираз: {entry['expression']}, Результат: {entry['result']}")
