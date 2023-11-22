import math 
class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie added")
    def __str__(self):
        return (f"{self.title} yazarı = {self.director}")
    def __len__(self):
        return self.duration
    def __del__(self):
        print("del objesi silindi")
m=Movie("Kırmızı Başlıklı Kız","ali",150)
print(f"Movie 1 = {m}  ")
print(len(m))
del m

class Person:
    #class attributes
    address='no information'
    #constructor(yapıcı metod)
    def __init__(self,name,year):
        #object attributes
        self.name=name
        self.year=year
        print("İnit metodu çalıştı")
    #instance methods
    def intro(self):#self girilmesi zorunlu
        print('Hello There I am '+self.name+" My age year "+str(self.year))
    def calculateAge(self):
        return 2023-self.year
#object (instance)
p1=Person("Tunay",2003)
p2=Person("Ahmet",2006)
#updating
p1.name="Ali" #artık değer "Tunay" yerine "Ali"
#accessing object attributes
print(f'name: {p1.name} year: {p1.year} adres: {p1.address}')
print(f'Name: {p2.name} My Age {p2.calculateAge()} My address {p2.address}')

class Circle:
    #class object attributes
    pi=math.pi
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
    #methods
    def cevre_hesapla(self):
        return 2*self.pi+self.yaricap
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
    
c1=Circle()#yaricap=1
c2=Circle(5)
#accessing object attributes
print(f'c1: alan= {c1.alan_hesapla()} c1: çevre= {c1.cevre_hesapla()}')
print(f'c2: alan= {c2.alan_hesapla()} c2: çevre= {c2.cevre_hesapla()}')
#Inheritance(kalıtım) : Miras alma
#Person=> name,lastname,age,eat(),run(),drink()
#Student(Person),Teacher(Person)
#Animal=> Dog(Animal),Cat(Animal)
class Person1():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print('Person Created')
    def who_am_i(self):
        print('i am a person')
class Student(Person1):
    def __init__(self,fname ,lname,number):
        Person1.__init__(self,fname,lname)
        self.number=number
        print('Student Created')
    #override
    def who_am_i(self):
        print('i am a student')
    def sayHello(self):
        print('hello i am a student')
class Teacher(Person1):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch=branch
    def who_am_i(self):
        print(f'i am a teacher {self.branch} öğretmeni')
p3=Person1('Tunay','bayındır')
s1=Student('Ali','Çıkmaz',550)
t1=Teacher('Ayşe','kuras',"matematik")
print(t1.firstname,' ',t1.lastname)
print(p3.firstname+' '+p3.lastname)
print(s1.firstname+' '+s1.lastname)
p3.who_am_i()
s1.who_am_i()
s1.sayHello()
t1.who_am_i()
#Question:
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Soru {self.questionIndex+1}: {question.text}')
        for q in question.choices:
            print('-'+q)
        answer=input('cevap: ')
        print(question.checkAnswer(answer))
        self.quess(answer)
        self.loadQuestion()
    def quess(self,answer):
        question=self.getQuestion()
        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def showScore(self):
        print('Score: ',self.score)
    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionIndex+1
        if questionNumber>totalQuestion:
            print("Quiz Bitti")
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,"*"))
q1=Question('En iyi programlama dili hangisidir ?',['C#','Python','Java'],'Python')
q2=Question('En popüler programlama dili hangisidir ?',['Python','C#','Java'],'Python')
q3=Question('En çok kazandıran programlama dili hangisidir ?',['Java','C#','Python'],'Python')
questions=[q1,q2,q3]
quiz=Quiz(questions)
quiz.loadQuestion()