class VeriBilimci():
    print("Bu Bir Sınıftır")

#özellik tanıyoruz

class VeriBilimci1():
    bolum=''
    sql='evet'

#özelliklere erişmek
print(VeriBilimci1.sql)

#özellik değiştirme
VeriBilimci1.sql="hayır"
print(VeriBilimci1.sql)

#sınıf örneklendirme
Ali = VeriBilimci1()
print(Ali.sql)
