class DataExplorer:
    def __init__(self, data):
        self.data = data

    def explore_data(self):
        extreme_values = self.find_extreme_values()
        print("Extreme Values:")
        print(extreme_values)

    def find_extreme_values(self):
        return self.data.describe(
            include=object
        )
