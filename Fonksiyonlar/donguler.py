#for
sayilar = [1,2,3,4,5,6]

for i in sayilar:
    print(i)
    
#maaşlara %20 yapan program

maaslar = [1000,2000,3000,4000]

def yeni_maas(x):
    print(x*20/100 + x)

for maas in maaslar:
    yeni_maas(maas)


#while

sayi = 1

while sayi <= 10:
    print(sayi)
    sayi +=1
