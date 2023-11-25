sozluk = {"bir":1,"iki":2}
print(sozluk)
print(type(sozluk))

#sozluk eleman seçme
print(sozluk["bir"])

#eleman değiştirme ve ekleme
#değiştirme
sozluk["bir"] = 11
print(sozluk)

#ekleme eğer yoksa ekler
sozluk["uc"] = 3
print(sozluk)