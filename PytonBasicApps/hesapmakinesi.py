import math

while True:
    print("""
    1. Toplama
    2. Çıkarma
    3. Çarpma
    4. Bölme
    """)
    islem=int(input("Yapmak İstediğiniz İşlemi Seçiniz: "))
    sayi1=int(input("Sayi1: "))
    sayi2=int(input("Sayi2: "))
    if (islem==1):
        print(sayi1+sayi2)
    elif (islem==2):
        print(sayi1-sayi2)
    elif (islem==3):
        print(sayi1*sayi2)
    elif (islem==4):
        print(math.fmod(sayi1,sayi2))
    else:
        print("Yanlış İşlem Yaptınız...")