class dator:

    def __init__(self):
        self.namn = "Inget namn"
        self.pris = 0
    
    def skriv_ut_pris(self):
        print("Namn: " + self.namn)
        print("Pris: " + str(self.pris) + "kr")

minDator = dator()
minDator.namn = "Plåtburk"
minDator.pris = 42

minDator.skriv_ut_pris()