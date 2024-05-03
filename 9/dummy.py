from tkinter import *
import random

class Dummy:

    def __init__(self, fonster):
        self.photo = PhotoImage(file= r"9/dummy.gif")
        self.label = Label(fonster, image=self.photo, borderwidth=0)
        self.posx = 3
        self.posy = 3

    def update(self):
        print("Dummy uppdaterar.")
        direction = random.randint(0, 4)
        if direction == 0:
            if self.posy < 10:
                self.posy += 1
            else:
                self.posy = 10
        elif direction == 1:
            if self.posx < 30:
                self.posx += 1
            else:
                self.posx = 30
        elif direction == 2:
            if self.posy > 0:
                self.posy -= 1
            else:
                self.posy = 0
        else:
            if self.posx > 0:
                self.posx -= 1
            else:
                self.posx = 0
        self.label.grid(column=self.posx, row=self.posy)
