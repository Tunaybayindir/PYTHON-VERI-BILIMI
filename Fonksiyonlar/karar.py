#True-False sorgulamaları

sinir = 4000
print(sinir == 5000)
print(sinir == 4000)

sicaklik = 25

if(sicaklik>30):
    print("Hava Çok Sıcak")
elif(sicaklik==25):
    print("Hava Güzel")
elif(sicaklik>0 and sicaklik<25):
    print("Hava Soğuyor")
else:
    print("YANLIŞ DEĞER GİRİLDİ!")