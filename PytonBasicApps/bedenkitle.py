#Problem 1
#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
boy=float(input("Boyunuzu girin(m): "))
kilo=int(input("Kilonuzu girin: "))
beden_kitle=kilo/boy**2
print("Beden Kitle İndeksiniz= ",beden_kitle)
if beden_kitle>30:
    print("OBEZ")
elif 30>=beden_kitle>25:
    print("Fazla Kilolu")
elif 25>=beden_kitle>18.5:
    print("Normal")
elif 18.5>beden_kitle:
    print("Zayıf")
else:
    print("Yanlış Değer Girdiniz")