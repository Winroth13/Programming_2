from tkinter import *
from livingThing import LivingThing
import random

class Animal(LivingThing):

    def __init__(self, width, height, list_of_objects, max_food) -> None:
        self.current_food = max_food
        super().__init__(width, height, list_of_objects)
    
    def baseUpdate(self, width, height):
        print("Animal uppdaterar.")
        self.move(width, height)
    
    def move(self, width, height):
        print("Animal flyttar.")
        direction = random.randint(0, 4)
        self.current_food -= 1
        if direction == 0:
            if self.posy < height - 1:
                self.posy += 1
        elif direction == 1:
            if self.posx < width - 1:
                self.posx += 1
        elif direction == 2:
            if self.posy > 0:
                self.posy -= 1
        else:
            if self.posx > 0:
                self.posx -= 1
        self.label.grid(column=self.posx, row=self.posy)