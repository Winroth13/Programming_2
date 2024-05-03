class Fiende:

    def __init__(self, hp = 0, hojd = 30, bredd = 30):
        self.bredd = bredd
        self.hojd = hojd
        self.hp = hp
    
    def info(self):
        print(f"Bredd: {self.bredd}\nHöjd: {self.hojd}\nHP: {self.hp}")

fiendeEtt = Fiende(7, 50)
fiendeTva = Fiende(10)

fiendeTva.info()