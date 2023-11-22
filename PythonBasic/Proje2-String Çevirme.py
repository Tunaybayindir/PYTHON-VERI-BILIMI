name="Tunay"
surname="Bayındır"
age=19

print("My Name Is "+name+' '+surname+' '+"and \nI am "+str(age)+' years old')
lenght=len(surname)#len(name) uzunluğu söyler

print(name[0])#0. indexteki elemanı alır yani T yi
print(lenght-1)#0 dan başladığı için -1 yaparız uzunluğu bulurken 
print(surname[-1])#sonuncu basamağı söyler
print(surname[2:5])#2 ile 5 arasını alır
print(name[2:])#2 den başlar sona kadar gider
print(name[:5]+" (baştan başlar 5 e kadar alır)")# baştan başlar 5 e kadar alır
print(surname[:8:2])#baştan başlar 8 e kadar gider 2 şer atlayarak
"""
index tanımlama = Tunay t(0) u(1) n(2) a(3) y(4)
\n alt satıra geçirir
str(age) int değeri stringe çevirir
float(age) int değeri floata çevirir
int(name) string değeri int'e çevirir
Tanımlarken name="tunay" veya name='tunay' yazabiliriz nokta kullanmayız.
Çoklu yorum satırı için 3 adet tırnak koyarız


"""
#tekli yorum satırı için # kullanırız
