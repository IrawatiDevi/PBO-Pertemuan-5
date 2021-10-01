class Tongkol:
    def __init__(self, kingdom, kelas):
        self.kingdom = kingdom
        self.kelas = kelas
    def spesies(self):
        print("Euthynnus affinis")
class Salmon:
    def __init__(self, kingdom, kelas):
        self.kingdom = kingdom
        self.kelas = kelas
    def spesies(self):
        print("Onchorhynchusn nerka")
tongkol1 = Tongkol("Animalia", "Pisces")
salmon1 = Salmon("Animalia", "Actinopterygii")
for ikan in (tongkol1, salmon1):
    ikan.spesies()
