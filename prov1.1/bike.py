class Bike:
    def __init__(self, model="Undefined", price=0):
        self.model = model
        self.price = price

    def showInfo(self):
        print(f"Model: {self.model}\nPrice: {self.price}")

    def getModel(self):
        return self.model

    def getPrice(self):
        return self.price
