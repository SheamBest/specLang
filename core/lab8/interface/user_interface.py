# Імпортуємо класи та модулі з інших файлів для взаємодії з різними аспектами аналізу даних.
from .methods.data_loader import DataLoader
from .methods.data_visualizations import VisualizationSelector
from .methods.data_preprocessor import DataPreprocessor
from .methods.data_explorer import DataExplorer
from .methods.base_visualization import BasicVisualizer
from .methods.advanced_visualization import AdvancedVisualizer
from .methods.subplots import MultipleSubplots
from .methods.export import Exporter

class DataAnalysisMenu:
    def __init__(self):
        # Ініціалізуємо об'єкт для завантаження даних.
        self.loader = DataLoader()
        # Ініціалізуємо об'єкт для обробки даних (поки не обрано конкретну операцію обробки).
        self.preprocessor = None

    def display_menu(self):
        # Відображення головного меню програми.
        menu_options = {
            1: "Explore Data",
            2: "Choose Visualizations",
            3: "Data Preprocessing",
            4: "Basic Visualization",
            5: "Advanced Visualization",
            6: "Create Subplots",
            7: "Export Visualization",
            8: "Exit"
        }

        print("Menu:")
        for num, option in menu_options.items():
            print(f"{num}. {option}")

    def explore_data(self):
        # Запуск режиму дослідження даних.
        explorer = DataExplorer(self.loader.data)
        explorer.explore_data()

    def choose_visualizations(self):
        # Запуск режиму вибору візуалізацій.
        visual_selector = VisualizationSelector(self.loader.data)
        visual_selector.choose_visualizations()

    def preprocess_data(self):
        # Запуск режиму попередньої обробки даних.
        self.preprocessor = DataPreprocessor(self.loader)
        self.preprocessor.preprocess()

    def basic_visualization(self):
        # Запуск режиму базової візуалізації (після попередньої обробки даних).
        if self.preprocessor:
            basic_visualizer = BasicVisualizer(self.preprocessor.processed_data)
            basic_visualizer.visualize()
        else:
            print("Data must be preprocessed first. Choose option 3 for Data Preprocessing.")

    def advanced_visualization(self):
        # Запуск режиму розширеної візуалізації (після попередньої обробки даних).
        if self.preprocessor:
            advanced_visualizer = AdvancedVisualizer(self.preprocessor.processed_data)
            advanced_visualizer.advanced_visualizations()
        else:
            print("Data must be preprocessed first. Choose option 3 for Data Preprocessing.")

    def create_subplots(self):
        # Запуск режиму створення піддіаграм (після попередньої обробки даних).
        if self.preprocessor:
            subplots_creator = MultipleSubplots(self.preprocessor.processed_data)
            subplots_creator.create_subplots()
        else:
            print("Data must be preprocessed first. Choose option 3 for Data Preprocessing.")

    def export_visualization(self):
        # Запуск режиму експорту візуалізації (після попередньої обробки даних).
        if self.preprocessor:
            exporter = Exporter(self.preprocessor.processed_data)
            exporter.export_visualization(file_format="png")
        else:
            print("Data must be preprocessed first. Choose option 3 for Data Preprocessing.")

    def run_menu(self):
        # Головний цикл програми для взаємодії з користувачем.
        while True:
            self.display_menu()
            choice = input("Enter the number of your choice: ")

            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    self.explore_data()
                elif choice == 2:
                    self.choose_visualizations()
                elif choice == 3:
                    self.preprocess_data()
                elif choice == 4:
                    self.basic_visualization()
                elif choice == 5:
                    self.advanced_visualization()
                elif choice == 6:
                    self.create_subplots()
                elif choice == 7:
                    self.export_visualization()
                elif choice == 8:
                    break  # Вихід з програми
                else:
                    print("Invalid choice. Please enter a valid number.")
            else:
                print("Invalid input. Please enter a number.")
