class CalculationHistory:
    def __init__(self):
        self.history = []

    def add(self, data):
        self.history.append(data)

    def show(self):
        for record in self.history:
            print(record)