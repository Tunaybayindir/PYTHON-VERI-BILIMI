#Problem 2
# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.    
a=int(input("Bir sayı girin: "))
b=int(input("Bir sayı girin: "))
c=int(input("Bir sayı girin: "))

if a>b and a>c:
    print("A büyüktür : ",a)
elif b>a and b>c:
    print("B büyüktür : ",b)
elif c>a and c>b:
    print("C büyüktür : ",c)
else:
    print("Yanlış Değer girdiniz")