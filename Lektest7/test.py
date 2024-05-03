class Rectangle:
    def __init__(self, name):
        self.width = 30
        self.height = 30
        self.name = name

    def printArea(self):
        print(f"Name: {self.name}\nArea: {self.width * self.height}")

rectangleA = Rectangle("A")
rectangleA.height = 50

rectangleB = Rectangle("B")
rectangleB.printArea()