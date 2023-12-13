import requests
import re
import json
import csv
import textwrap
from prettytable import PrettyTable
import os

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        # Виконує GET-запит до вказаної точки (endpoint) API і повертає відповідь у форматі JSON
        response = requests.get(self.base_url + endpoint)
        return response.json()

def prompt_for_endpoint():
    # Перепитує користувача про введення точки (endpoint) API
    return input("Please enter the endpoint ('posts', 'comments', etc.): ")

def parse_input(input_string):
    # Використовує регулярний вираз для пошуку дат у введеному рядку
    dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', input_string)
    return dates

def display_data(data):
    if not data:
        print("No data available to display.")
        return

    if isinstance(data[0], dict):
        # Створює PrettyTable для відображення даних у вигляді таблички
        table = PrettyTable(field_names=data[0].keys())
    else:
        print("Data format is not recognized.")
        return

    for item in data:
        # Заповнює табличку даними, обгортаючи значення для кращого відображення
        row = [textwrap.fill(str(value), width=50) for value in item.values()]
        table.add_row(row)

    print(table)

def save_data(data, format):
    # Визначаємо шлях до папки 'output', яка знаходиться на рівень вище
    output_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'output')

    # Створюємо папку, якщо вона ще не існує
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Визначаємо шлях до файлу у папці 'output' та зберігаємо дані у вказаному форматі (json або csv)
    if format == 'json':
        file_path = os.path.join(output_dir, 'data.json')
        with open(file_path, 'w') as f:
            json.dump(data, f)
    elif format == 'csv':
        file_path = os.path.join(output_dir, 'data.csv')
        with open(file_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

def safe_api_request(callable, *args, **kwargs):
    try:
        # Викликає функцію callable з переданими аргументами та оброблює винятки
        return callable(*args, **kwargs)
    except requests.RequestException as e:
        print(f"An error occurred during API request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
