import os
from .data_loader import DataLoader
from .data_preprocessor import DataPreprocessor
import matplotlib.pyplot as plt

# Отримайте абсолютний шлях до файлу CSV
csv_file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "data", "data.csv")
)

loader = DataLoader(csv_file_path=csv_file_path)
data = loader.data

preprocessor = DataPreprocessor(loader)
preprocessor.preprocess()


class BasicVisualizer:
    def __init__(self, data):
        self.data = data

    def visualize(self):
        plt.plot(self.data["age"], self.data["job"], "o")
        plt.xlabel("Age")
        plt.ylabel("Job")
        plt.title("Basic Visualization")
        plt.show()
