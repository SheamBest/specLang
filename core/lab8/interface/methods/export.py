import matplotlib.pyplot as plt
from .data_loader import DataLoader
from .data_preprocessor import DataPreprocessor
import os

# Завантажте дані, наприклад, з файлу generated_data.csv
csv_file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..","..", "data", "data.csv")
)

loader = DataLoader(csv_file_path=csv_file_path)
data = loader.data

preprocessor = DataPreprocessor(loader)
preprocessor.preprocess()


class Exporter:
    def __init__(self, data):
        self.data = data

    def export_visualization(self, file_format="png"):
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Created folder: {output_folder}")

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(self.data["age"], self.data["job"], "o")
        ax.set_xlabel("Age")
        ax.set_ylabel("Job")
        ax.set_title("Exported Visualization")

        file_name = f"exported_visualization.{file_format}"
        file_path = os.path.join(output_folder, file_name)

        plt.savefig(file_path)
        print(f"Visualization saved to {file_path}")

