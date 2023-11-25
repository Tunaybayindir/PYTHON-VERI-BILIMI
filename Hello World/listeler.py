#listeler
#nasıl oluşturulur
#[] - list()

notlar = [10,20,30,40,[50,30,40]]

print(type(notlar))
print(len(notlar))

#liste içinde gezinme
print(notlar[0])
#liste içindeki listeye erişmek
print(notlar[4][1])
#listeyi silme
# del notlar
# print(notlar)

#değer değiştirme
notlar[0] = 20
del notlar[1]
print(notlar) 

#append remove
notlar.append(500)
print(notlar)
notlar.remove(500)
print(notlar)

#indekse göre eleman ekleme insert()
notlar.insert(0,5000)
print(notlar)

#pop
notlar.pop()
#sondakini siler
#indekse göre siler
notlar.pop(4)
print(notlar)