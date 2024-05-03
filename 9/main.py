from tkinter import *
from dummy import Dummy
from plant import Plant
from sheep import Sheep
from wolf import Wolf

time_between_updates = 1000  # i millisekunder

width  = 10  # antal rutor
height = 30  # antal rutor
max_food = 10 # maxiam mängd mat
grow_time = 3

fonster = Tk()

empty = PhotoImage(file= r"9/empty.gif")

#Skapar kartan
for i in range(width):
    for j in range(height):
        etikett = Label(fonster, image=empty, borderwidth=0)
        etikett.grid(column=i, row=j)

#Skapar objekten på skärmen
list_of_objects = []

for i in range(10):
    plant = Plant(fonster, width, height, list_of_objects, grow_time)
    list_of_objects.append(plant)
    sheep = Sheep(fonster, width, height, list_of_objects, max_food)
    list_of_objects.append(sheep)
    wolf = Wolf(fonster, width, height, list_of_objects, max_food)
    list_of_objects.append(wolf)

#Uppdaterar objekten
def update_all_objects():
    for object in list_of_objects:
        object.update(width, height, list_of_objects)

    fonster.after(time_between_updates, update_all_objects)


fonster.after(time_between_updates, update_all_objects)

fonster.mainloop()
