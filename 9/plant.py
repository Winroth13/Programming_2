from tkinter import *
from livingThing import LivingThing
import random

class Plant(LivingThing):

    def __init__(self, fonster, width, height, list_of_objects, grow_time) -> None:
        self.photo = PhotoImage(file= r"9/plant.gif")
        self.label = Label(fonster, image=self.photo, borderwidth=0)
        self.grow_time = grow_time
        self.time = 0
        self.fonster = fonster
        super().__init__(width, height, list_of_objects)
    
    def update(self, width, height, list_of_objects):
        print("Plant uppdaterar.")
        self.time += 1
        if self.grow_time == self.time:
            new_plant_posx = 0
            new_plant_posy = 0
            direction = random.randint(0, 4)
            if direction == 0:
                if self.posy < height - 1:
                    new_plant_posy = self.posy + 1
                    new_plant_posx = self.posx
            elif direction == 1:
                if self.posx < width - 1:
                    new_plant_posy = self.posy
                    new_plant_posx = self.posx + 1
            elif direction == 2:
                if self.posy > 0:
                    new_plant_posy = self.posy - 1
                    new_plant_posx = self.posx
            else:
                if self.posx > 0:
                    new_plant_posy = self.posy
                    new_plant_posx = self.posx - 1
            tile_occupied = False
            for object in list_of_objects:
                if new_plant_posx == object.posx and new_plant_posy == object.posy:
                    tile_occupied = True
            if tile_occupied == False:
                new_plant = Plant(self.fonster, width, height, list_of_objects, self.grow_time)
                new_plant.posx = new_plant_posx
                new_plant.posy = new_plant_posy
                new_plant.label.grid(column=new_plant.posx, row=new_plant.posy)
                list_of_objects.append(new_plant)