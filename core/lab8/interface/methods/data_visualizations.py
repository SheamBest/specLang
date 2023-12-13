import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class VisualizationSelector:
    def __init__(self, data):
        self.data = data

    def choose_visualizations(self):
        self.plot_histogram()
        self.plot_scatter_plot()
        self.plot_pie_chart()

    def plot_histogram(self):
        plt.figure(figsize=(8, 6))
        self.data["date-of-birth"] = pd.to_datetime(self.data["date-of-birth"])
        self.data["year_of_birth"] = self.data["date-of-birth"].dt.year
        sns.histplot(self.data["year_of_birth"], bins=20, kde=True)
        plt.title("Histogram of Birth Years")
        plt.xlabel("Birth Year")
        plt.ylabel("Frequency")
        plt.show()

    def plot_scatter_plot(self):
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x="date-of-birth", y="job", data=self.data)
        plt.title("Scatter Plot: Date of Birth vs Job")
        plt.xlabel("Date of Birth")
        plt.ylabel("Job")
        plt.show()

    def plot_pie_chart(self):
        plt.figure(figsize=(8, 6))
        self.data["sex"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90)
        plt.title("Pie Chart: Gender Distribution")
        plt.show()
