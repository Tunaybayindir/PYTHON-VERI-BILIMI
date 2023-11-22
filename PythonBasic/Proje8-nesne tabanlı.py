#class
class Person:
    
    #class atributes
    address="no information"
    #constructor (yapıcı metod)
    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("init metodu çalıştı")
    #methods
    def intro(self):
        print("Hello There I am "+self.name)
    def calculateAge(self):
        return 2023-self.year
    
class Cars:
    def __init__(self,name,model,year) :
        self.name=name
        self.year=year
        self.model=model
        
class Circle:
    pi=3.14
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
        
    def cevre_hesapla(self):
        return 2 * self.pi +self.yaricap
    def alan_hesapla(self):
        return self.pi *(self.yaricap**2)

c1=Circle() #yaricap 1
c2=Circle(5)


print(f"Yaricapı {c1.yaricap} olan, cevresi : {c1.cevre_hesapla()} alanı : {c1.alan_hesapla()}")
print(f"Yaricapı {c2.yaricap} olan, cevresi : {c2.cevre_hesapla()} alanı : {c2.alan_hesapla()}")



car1=Cars("Honda","Yumurta kasa",1998)

print(f"Car1: Name : {car1.name} Model : {car1.model} year : {car1.year}")
        


p1=Person("tunay",2003)
p2=Person("ali",2000)
p2.intro()

print(f"P1: Adım :{p1.name} yaşım : {p1.calculateAge()}")
print(f"p2: Name : {p2.name} yaşım : {p2.calculateAge()}")
print(f"P1: Name : {p1.name} Year : {p1.year}")
print(f"P1: Name : {p2.name} Year : {p2.year}")
