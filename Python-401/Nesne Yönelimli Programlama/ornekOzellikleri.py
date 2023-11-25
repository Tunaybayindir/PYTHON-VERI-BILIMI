class VeriBilimci():
    def __init__(self):
        self.bildigi_diller=["python"]
        self.bolum = "programlama"

ali = VeriBilimci()
print(ali.bildigi_diller)

class VeriBilimci1():
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum =""
    def dil_ekle(self,ekle_dil):
        self.bildigi_diller.append(ekle_dil)
        
ahmet = VeriBilimci1()
print("Ahmetin Bildiği Diller: ",ahmet.bildigi_diller)
ahmet.dil_ekle("türkçe")
print("Ahmetin Bildiği Diller: ",ahmet.bildigi_diller[0])