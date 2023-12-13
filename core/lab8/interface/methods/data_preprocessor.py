import pandas as pd
from .data_loader import DataLoader


class DataPreprocessor:
    def __init__(self, data_loader):
        data_loader = DataLoader()
        self.data_loader = data_loader
        self.processed_data = (
            None  # Ініціалізуємо як None, оскільки поки що немає оброблених даних
        )

    def preprocess(self):
        # Використовуйте self.data_loader.data, оскільки це атрибут, який ми завантажуємо з класу DataLoader
        self.processed_data = self.data_loader.data.copy()

        self.processed_data["age"] = (
            pd.to_datetime("now") - pd.to_datetime(self.processed_data["date-of-birth"])
        ).apply(lambda x: x.days // 365)
        self.processed_data["date-of-birth"] = pd.to_datetime(
            self.processed_data["date-of-birth"]
        )
