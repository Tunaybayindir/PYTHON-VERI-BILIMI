class Araba():
    def __init__(self,model="Bilgi Yok",beygir=70,silindir=4):
        self.model=model
        self.beygir=beygir
        self.silindir=silindir



araba=Araba("Hyundai",110,5)
print(araba.model)
print(araba.beygir)
print(araba.silindir)
araba1=Araba("Renault",150,6)
print(araba1.model)
print(araba1.beygir)
print(araba1.silindir)