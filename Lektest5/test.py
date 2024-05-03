import random

class Tarning:

    def __init__(self):
        self.slaOm()
    
    def slaOm(self):
        self.varde = random.randint(1, 6)

antalTarningar = 1000
tarningslista = []
summa = 0

for i in range(antalTarningar):
    nyTarning = Tarning()
    tarningslista.append(nyTarning)

for tarning in tarningslista:
    if tarning.varde == 1:
        tarning.slaOm()
    summa += tarning.varde

print(f"Medelvärdet: {summa/len(tarningslista)}")
