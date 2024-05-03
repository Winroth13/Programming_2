from tkinter import *
from animal import Animal
from plant import Plant

class Sheep(Animal):

    def __init__(self, fonster, width, height, list_of_objects, max_food) -> None:
        self.max_food = max_food
        self.photo = PhotoImage(file= r"9/sheep.gif")
        self.label = Label(fonster, image=self.photo, borderwidth=0)
        super().__init__(width, height, list_of_objects, max_food)
    
    def update(self, width, height, list_of_objects):
        print("Sheep uppdaterar.")
        self.baseUpdate(width, height)
        self.eat(list_of_objects)
        
    def eat(self, list_of_objects):
        for object in list_of_objects:
            if self.posx == object.posx and self.posy == object.posy and type(object) == Plant:
                list_of_objects.remove(object)
                object.label.grid_forget()
                self.current_food = self.max_food
        if self.current_food == 0:
            list_of_objects.remove(self)
            self.label.grid_forget()
