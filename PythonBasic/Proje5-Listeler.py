message='hello there. my name is tunay baywndwr'

# print(message)
# print("1. mesaj direkt")
message=message.title()
# print(message)
# print("2. mesaj baş harfleri büyüttü")
message=message.replace('i','I').replace('w','ı')
# print(message)
# print("3. mesaj i yerine I ve w yerine ı koydu")
message=message.split()
print(message)
# print("son mesaj dizilere ayırdı")

list1=["one","two","three"]
list2=["four","five",",six"]

number=list1+list2
print(number)
lenght=len(number)
print(lenght)
print(number[2])

user1=["Sadık",35]
user2=["Tunay",19]
users=[user1,user2]
print(users)
print(user1)
username=user1
print("1. kullanıcının ismi = "+username[0]) 
# username oluşturduk ve 1. kullanıcının indexini attık oradan 0. indexi aldık ismini
print("2. kullanıcının ismi = "+users[1][0]) 
# 1. indexin içindeki 0. indexi aldık