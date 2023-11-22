class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgiGoster(self):
        print(""" 
        İsim: {}
        
        Soyisim: {}
        
        Numara: {}
        
        Maaş: {}
        
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))


user1 = Yazilimci("Tunay","Bayındır",555,5500,["Türkçe","İngilizce"])
user1.bilgiGoster()