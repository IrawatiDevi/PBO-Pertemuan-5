class Ikan:
    def intro(self):
        print("Ikan adalah anggota vertebrata poikilotermik yang hidup di air dan bernapas dengan insang.")
    def spesies(self):
        print("Ikan memiliki berbagai jenis spesies yang berbeda.")
class Tongkol(Ikan):
    def spesies(self):
        print("Tongkol spesiesnya adalah Euthynnus affinis")
class Salmon(Ikan):
    def spesies(self):
        print("Salmon bukan spesies Euthynnus affinis")

obj_Ikan = Ikan()
obj_tongkol = Tongkol()
obj_salmon = Salmon()
print("=========================================================")
obj_Ikan.intro()
obj_Ikan.spesies()
print("=========================================================")
obj_tongkol.intro()
obj_tongkol.spesies()
print("=========================================================")
obj_salmon.intro()
obj_salmon.spesies()
print("=========================================================")