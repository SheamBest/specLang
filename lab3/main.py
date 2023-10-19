import art
from termcolor import colored

# Функція отримання вводу від користувача з можливістю задати значення за замовчуванням
def get_user_input(prompt, default=None):
    user_input = input(prompt).strip()
    return user_input if user_input else default

# Функція генерації ASCII-арту з можливістю зазначення стандартного шрифту
def get_art(text, font_name):
    try:
        return art.text2art(text, font=font_name)
    except Exception as e:
        print(f"Помилка: {e}")
        return art.text2art(text, font='block')

# Функція вибору кольору
def get_color():
    colors = {
        'червоний': 'red',
        'синій': 'blue',
        'зелений': 'green'
    }
    color_name = input("Виберіть колір тексту (червоний/синій/зелений): ").lower()
    return colors.get(color_name, 'white')

# Функція вибору розміру ASCII-арту з можливістю значень за замовчуванням
def get_size():
    try:
        width = int(input("Введіть ширину ASCII-арту: "))
        height = int(input("Введіть висоту ASCII-арту: "))
    except ValueError:
        width, height = 80, 20
    return width, height

# Головна функція
def main():
    text = get_user_input("Введіть слово або фразу для генерації ASCII-арту: ")
    font_name = get_user_input("Виберіть шрифт (стандартний/керований/блоки): ")

    art_object = get_art(text, font_name)

    color = get_color()
    width, height = get_size()

    char = input("Введіть символ, який ви хочете використовувати (наприклад, '@', '#', '*'): ")

    # Форматування та відображення ASCII-арту
    colored_art = colored(art_object, color)
    print("Попередній перегляд вашого ASCII-арту:")
    formatted_art = colored_art.center(width).replace(' ', char)
    print(formatted_art)

    save_option = input("Зберегти ASCII-арт у файл? (так/ні): ").lower()
    if save_option == 'так':
        file_name = input("Введіть ім'я файлу для збереження: ")
        with open(file_name, 'w') as file:
            file.write(formatted_art)
            print(f"ASCII-арт був збережений у файлі '{file_name}'")

if __name__ == "__main__":
    main()
