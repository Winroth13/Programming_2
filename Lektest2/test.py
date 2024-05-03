class Bil():

    def __init__(self, vikt = 0, pris = 0, farg ="Inget satt", regNummer = "Inget satt"):
        self.vikt = vikt
        self.pris = pris
        self.farg = farg
        self.regNummer = regNummer

class LastBil(Bil):
    
    def __init__(self, vikt = 0, pris = 0, farg ="Inget satt", regNummer = "Inget satt", lastutrymme = 0):
        self.lastutrymme = lastutrymme
        super().__init__(vikt, pris, farg, regNummer)

minBil = Bil(1200, 95000, "Röd", "ABC123")
minLastbil = LastBil(12000, 3500000, "vit", "DBC321", 950)