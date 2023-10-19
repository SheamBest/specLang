import math  # Імпортуємо бібліотеку для обчислення квадратного кореня, піднесення до степеня та знаходження відсотка

# Налаштування користувача
decimal_places = 2  # Кількість десяткових розрядів за замовчуванням
memory = 0  # Ініціалізуємо пам'ять значенням 0
history = []  # Ініціалізуємо список для збереження історії обчислень

while True:
    try:
        if history:
            print("Історія обчислень:")
            for i, entry in enumerate(history, 1):
                print(f"{i}. Вираз: {entry['expression']}, Результат: {entry['result']}")

        # Просимо користувача ввести перше число
        num1 = float(input("Введіть перше число: "))

        # Просимо користувача ввести друге число
        num2 = float(input("Введіть друге число: "))

        while True:
            # Просимо користувача ввести оператор (+, -, *, /, ^, √, %, M - для збереження в пам'ять, D - для зміни десяткових розрядів)
            operator = input("Введіть оператор (+, -, *, /, ^, √, %, M - для збереження в пам'ять, D - для зміни десяткових розрядів): ")

            # Перевіряємо чи оператор є допустимим (+, -, *, /, ^, √, %, M, D)
            if operator in ('+', '-', '*', '/', '^', '√', '%', 'M', 'D'):
                break  # Виходимо з циклу, якщо оператор коректний
            else:
                print("Помилка! Введіть дійсний оператор (+, -, *, /, ^, √, %, M, D).")

        # Змінюємо кількість десяткових розрядів за бажанням користувача
        if operator == "D":
            decimal_places = int(input("Введіть кількість десяткових розрядів: "))
            continue  # Перейти до наступної ітерації циклу

        # Проводимо обчислення залежно від обраного оператора
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            # Перевіряємо, щоб уникнути ділення на нуль
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе.")
            result = num1 / num2
        elif operator == "^":
            result = num1 ** num2
        elif operator == "√":
            # Використовуємо функцію math.sqrt для обчислення квадратного кореня
            result = math.sqrt(num1)
        elif operator == "%":
            result = num1 % num2
        elif operator == "M":
            memory = result = 0
            print(f"Значення {memory} збережено в пам'яті.")

        # Форматуємо результат з вказаною кількістю десяткових розрядів
        formatted_result = round(result, decimal_places)

        # Виводимо результат обчислення
        print(f"Результат обчислення: {formatted_result}")

        # Додаємо запис до історії обчислень
        history_entry = {'expression': f"{num1} {operator} {num2}", 'result': formatted_result}
        history.append(history_entry)

    except ValueError:
        print("Помилка! Введено недійсне число.")
    except ZeroDivisionError as e:
        print(f"Помилка: {e}")

    # Питаємо користувача, чи він хоче виконати ще одне обчислення
    repeat = input("Виконати ще одне обчислення? (Так/Ні): ").lower()
    if repeat != "так":
        break  # Виходимо з головного циклу, якщо користувач відповів "ні"

# Виводимо історію обчислень при завершенні програми
print("Історія обчислень:")
for i, entry in enumerate(history, 1):
    print(f"{i}. Вираз: {entry['expression']}, Результат: {entry['result']}")