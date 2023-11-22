# list=[1,2,3,1,2,1,1,1,1,2,3,4,5]
# list.append(4)
# list.pop()


# print("1 Rakamının sayısı =",list.count(1))
# print(type(list))
# print(list)


# def total(num1,num2):
#     return num1+num2

# def SayHello():
#     print("Hello")

# print(total(10,20))
# SayHello() 


# def yasHesapla(dogumyili):
#     return 2023 - dogumyili  

# print(yasHesapla(2003),"Yaşındasınız Tunay Bey")


# def emekliligeKacYilKaldi(dogumyili):
#     yas=yasHesapla(dogumyili)
#     emeklilik=65-yas
    
#     if emeklilik>0:
#         print(f'Emekliliğinize {emeklilik} yıl kaldı')
#     else:
#         print("zaten Emeklisiniz")
        
# print(emekliligeKacYilKaldi(2003))

# sehirler=["istanbul","ardahan"] 

# def change(n):
#     n[0]="ankara"

# change(sehirler)
# print(sehirler)

# def user(a,b,c,*args,**kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)

# user(10,20,30,60,70,80,90,key="Name",key1="tunay")
# print(user)


# def change(n):
#     n[0]="istanbul"
    
# city=["ankara","erdek"]

# change(city)

# print(city)


#1.gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# t=input("bir kelime girin = ")
# a=int(input("kaç defa yazdırılsın = "))
# def change(t):
    
#     for i in range(1,a+1):
#         print(i,"kere yazdırıldı",t)
        

# change(t)

# def yazdir(kelime,sayi):
#     print(kelime*sayi)

# yazdir("Tunay\n",10)


#2. Kendisine gönderilen sınırsız sayıdaki parametreyi bir listeye çevirme

# def cevir(*params):
#     liste=[]
#     for param in params:
#         liste.append(param)
        
#     return liste
# result=cevir(10,20,30,40,"Tunay")
# print(result)

#3.gönderilen 2 sayı arasındaki tüm asal sayıları bulun


# sayi1=int(input("ilk sayı = "))
# sayi2=int(input("ikinci sayı = "))

# def sayi(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if (sayi%i==0):
#                     break
#             else:
#                 print(sayi)
                
                
# sayi(sayi1,sayi2)
                    
                    
                    
#4. kendisine gönderilen bir sayının tam bölenlerini bulan

# def tambolen(sayi):
#     tambolenliste=[]
    
#     for i in range(2,sayi+1):
#         if (sayi % i==0):
#             tambolenliste.append(i)
#     return tambolenliste

# print(tambolen(100))


# numbers=[1,3,4,5,6,7,8,9]


# def check_even(num): return num%2==0

# # result=list(filter(lambda num:num%2==0,numbers))
# result=list(filter(check_even,numbers))


# # print(result)
# name="ali"

# def changeName(new_name):
#     name=new_name
#     print(name)
    
# changeName("Tunay")

# print(name)


x=50
def test():
    global x
    print(f"x : {x}")
    x=100
    print(f"changed x to {x}")
test()

print(x)