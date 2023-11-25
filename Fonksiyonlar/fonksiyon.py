#fonksiyon nasıl yazılır

def kare_al(x):
    print(x**2)
    
kare_al(5)

#bilgi notuyla beraber yazmak
def kare_al(x):
    print("Girilen Sayının Karesi: " + str(x**2))
kare_al(5)

#2 argünmanlı fonksiyon yazma

def carp(x,y):
    print(x*y)
carp(2,3)
#on tanımlı argünmanlar
def carp(x,y=1):
    print(x*y)
carp(3)

#sıralama
def carp(x,y):
    print(x*y)
carp(y=3,x=2)