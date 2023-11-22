isim=input("isminiz : ")
cinsiyet=input("Cinsiyetinizi giriniz (k/e): ")
yas=int(input("Yaşınız : "))


if(yas>=18) and (cinsiyet=='E' or cinsiyet=='e'):
   print("Askere Gidebilirsiniz "+ isim + " Bey")
elif(yas>18) and (cinsiyet=='k' or cinsiyet=='K'):
   print("Kadınlar Askere Gidemez")
elif(yas<18) and (cinsiyet=='E' or cinsiyet=='e'):
   print("yaşınız tutmuyor "+ isim +"Bey")
else:
   print("askere gidemezsiniz")