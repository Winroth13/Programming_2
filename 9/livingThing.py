import random

class LivingThing:

    def __init__(self, width, height, list_of_objects):
        while True: 
            tile_occupied = False
            new_posx = random.randint(0, width - 1)
            new_posy = random.randint(0, height - 1)
            for object in list_of_objects:
                if new_posx == object.posx and new_posy == object.posy:
                    tile_occupied = True
            if tile_occupied == False:
                self.posx = new_posx
                self.posy = new_posy
                self.label.grid(column=self.posx, row=self.posy)
                break
    
    def set_position(self, x, y):
        self.posx = x
        self.posy = y
        self.label.grid(column=self.posx, row=self.posy)