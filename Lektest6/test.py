import random


class Rektangel:
    def __init__(self, hojd=0):
        self.bredd = 100
        self.hojd = hojd

    def area(self):
        return self.bredd * self.hojd


antalRektanglar = 100

rektangellista = [Rektangel(random.randint(1, 500)) for _ in range(antalRektanglar)]

areaLista = [rektangel.area() for rektangel in rektangellista]

[print(f"Area: {area}") for area in areaLista if area > 45000]
