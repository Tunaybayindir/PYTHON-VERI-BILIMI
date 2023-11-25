#return

#print ile atayamayız none çıkar
def kare(x,y):
    print(x*y)
# kare(3,2)
kare_al= kare(3,2)
print(kare_al)

#Return ile atayıp işlem yapabiliriz
def kare(x,y):
    return x*y
kare_al = kare(3,2)
print(kare_al)

#global değişkenler
x=10
y=20
def kare(x,y):
    #local değişkenler de bunlar
    print(x*y)