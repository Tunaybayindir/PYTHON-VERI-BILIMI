# def outer(num1):
    
#     def inner(num1):
#         return num1+1
#     num2=inner(num1)
#     print(num2)

# outer(10)


# liste =[1,2,3,4,5]
# iterator =iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# alttaki ve üsteki aynı çıktıyı verir
# while True:
#     try:
#         element=next(iterator)
#         print(element)
#     except StopIteration:
#         break

# class MyNumbers:
#     def __init__(self,start,stop):
#         self.start=start
#         self.stop=stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start <= self.stop:
#             x= self.start
#             self.start +=1
#             return x
#         else:
#             raise StopIteration

# list=MyNumbers(10,20)
# for x in list:
#     print(x)

# def cube():
#     result=[]
#     for i in range(5):
#         result.append(i**3)
#     return result

# print(cube())


def cube():
    for i in range(5):
        yield i ** 3
        
genarator=cube()
iterator=iter(genarator)
print(next(iterator))
print(next(iterator))