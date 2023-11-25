a=10
b="2"
try:
   print(a/b)
except ZeroDivisionError:
    print("payda 0 olamaz")
except TypeError:
    print("İnteger değer stringe bölünemez")