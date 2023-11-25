#set oluşturma
#kümelere benzer

s = set()
#her değerin 1 ini alır sadece 
#setler sırasızdır
at = "ali_topu"
t = set(at)
print(t)

#ekleme çikarma
liste= ["yaz","deftere"]

setol = set(liste)
print(setol)
#ekleme
setol.add("tahtaya")
print(setol)
#cıkarma
setol.remove("yaz")
print(setol)

#difference
set1 = set([1,5,3])
set2 = set([1,2,3])
#set1 de olup 2 de olmayanı verir
print(set1.difference(set2))

#intersection & union
#2 kümenin kesişimini verir 
print(set1.intersection(set2))
#intersection_update() günceller 

#2 kümenin birleşimini alır her eleman 1 defa alınır
print(set1.union(set2))

#aynı olanları çıkarır farklılar kalır
print(set1.symmetric_difference(set2))
