#yorum satırı
#SAYILAR VE STRİNGLERE GİRİŞ
print(type(9))
print(type(9.2))
print(type(3>5))
print(type("hello"))
print(9+9)
print(9*9)

#STRİNG
print(type(123))
print(type('123'))
a = "123"
cumle = "tunay bayındır"
#len
print(len(a))

#büyük yazar
print(cumle.upper())
#küçük yazar
print(cumle.lower())
#küçükse true yazar
print(cumle.islower())

#replace 
cumle2 = "*mamlakat_fana*"
print(cumle2.replace("a","e"))

#strip yanlardan silinme
print("-----------------------------")
print(cumle2.strip("*"))

#dir

print(dir(str))
#kümeler
print(cumle[0])
print(cumle[1])
print(cumle[3:5])
print(cumle[-1:])

