# Problem 1
# Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
# boy=float(input("Boyunuzu girin(m): "))
# kilo=int(input("Kilonuzu girin: "))
# beden_kitle=kilo/boy**2
# print("Beden Kitle İndeksiniz= ",beden_kitle)
# if beden_kitle>30:
#     print("OBEZ")
# elif 30>=beden_kitle>25:
#     print("Fazla Kilolu")
# elif 25>=beden_kitle>18.5:
#     print("Normal")
# elif 18.5>beden_kitle:
#     print("Zayıf")
# else:
#     print("Yanlış Değer Girdiniz")

#Problem 2
# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.    
# a=int(input("Bir sayı girin: "))
# b=int(input("Bir sayı girin: "))
# c=int(input("Bir sayı girin: "))

# if a>b and a>c:
#     print("A büyüktür : ",a)
# elif b>a and b>c:
#     print("B büyüktür : ",b)
# elif c>a and c>b:
#     print("C büyüktür : ",c)
# else:
#     print("Yanlış Değer girdiniz")

# Problem 3
# Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
ogrenci_sayisi=int(input("Kaç Öğrenci Girişi yapacaksınız"))
while ogrenci_sayisi>0:
    vize1=int(input("Vize Notunuz: "))
    vize2=int(input("Vize 2. Notunuz: "))
    final=int(input("Final Notunuz: "))
    ortalama=vize1*0.3 + vize2*0.3 +final*0.4

    if ortalama>=90:
        print("AA")
    elif ortalama>=85:
        print("BA")
    elif ortalama>=80:
        print("BB")
    elif ortalama>=75:
        print("CB")
    elif ortalama>=70:
        print("CC")
    elif ortalama>=65:
        print("DC")
    elif ortalama>=60:
        print("DD")
    elif ortalama>=55:
        print("FD")
    elif ortalama>=50:
        print("FF")
    else:
        print("Geçersiz Değer Girdiniz")
    ogrenci_sayisi =ogrenci_sayisi-1