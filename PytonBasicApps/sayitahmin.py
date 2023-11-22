import random
import time


tahmin_hakki=5
rastgele_sayi=random.randint(1,40)


while True:
    sayi=int(input("Tahmininiz: "))
    if (sayi<rastgele_sayi):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha Yüksek Sayı giriniz.")
    elif(sayi>rastgele_sayi):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha Düşük Bir Sayı Giriniz.")
    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler...Tahmininiz Doğru Sayı:",rastgele_sayi)
        break
    if (tahmin_hakki==0):
        print("Hakkınız Bitmiştir...")
        break