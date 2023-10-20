

i=1
while i<10:
     print(i)
     if i==3:
      break
     i +=1
x=lambda  a,b:a*b
print(x(5,10))

akib=lambda a,b: a-b
print(akib(20,30))
def myfunction(n):
    return lambda a: a*n
akib=myfunction(5)
print(akib(10))
class MyClass:
     def __init__(self,name,age):
         self.age=age
         self.name=name
p1=MyClass("Akib",10)
print(p1.name)
print(p1.age)

