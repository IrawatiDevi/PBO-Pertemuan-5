class kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bersuara(self):
        print("meow")
class dog:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bersuara(self):
        print("guk...guk...")
kucing1 = kucing("Tom", 3)
anjing1 = dog("Spike", 4)
for hewan in (kucing1, anjing1):
    hewan.bersuara()