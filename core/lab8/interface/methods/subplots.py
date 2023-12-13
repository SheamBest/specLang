import seaborn as sns
import matplotlib.pyplot as plt
from .data_loader import DataLoader
from .data_preprocessor import DataPreprocessor
import os

csv_file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "data", "data.csv")
)

loader = DataLoader(csv_file_path=csv_file_path)
data = loader.data


preprocessor = DataPreprocessor(loader)
preprocessor.preprocess()


class MultipleSubplots:
    def __init__(self, data):
        self.data = data

    def create_subplots(self):
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

        sns.histplot(self.data["age"], bins=20, kde=True, ax=axes[0, 0])
        axes[0, 0].set_title("Histogram of Age")
        axes[0, 0].set_xlabel("Age")
        axes[0, 0].set_ylabel("Frequency")

        sns.scatterplot(x="age", y="job", data=self.data, ax=axes[0, 1])
        axes[0, 1].set_title("Scatter Plot: Age vs Job")
        axes[0, 1].set_xlabel("Age")
        axes[0, 1].set_ylabel("Job")

        self.data["sex"].value_counts().plot.pie(
            autopct="%1.1f%%", startangle=90, ax=axes[1, 0]
        )
        axes[1, 0].set_title("Pie Chart: Gender Distribution")

        fig.suptitle("Multiple Subplots")
        plt.show()
