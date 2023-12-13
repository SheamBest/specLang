import seaborn as sns
import matplotlib.pyplot as plt
from .data_loader import DataLoader
from .data_preprocessor import DataPreprocessor
import os

class AdvancedVisualizer:
    def __init__(self, data):
        self.data = data

    def advanced_visualizations(self):
        plt.ion()
        plt.figure(figsize=(12, 8))
        sns.heatmap(self.get_numeric_data().corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Теплова карта кореляцій")
        plt.show()

    def get_numeric_data(self):
        loader = self.load_data()
        return loader.data.select_dtypes(include="number")

    def load_data(self):
        csv_file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "data", "data.csv")
        )
        loader = DataLoader(csv_file_path=csv_file_path)
        data = loader.data
        preprocessor = DataPreprocessor(loader)
        preprocessor.preprocess()
        return loader

# Створюємо екземпляр AdvancedVisualizer з даними
csv_file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "data", "data.csv")
)
loader = DataLoader(csv_file_path=csv_file_path)
data = loader.data
visualizer = AdvancedVisualizer(data)
