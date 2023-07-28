class Student:
    def __init__(self,name):
        self.name=name
    #overloading the strig method
    def __str__(self):
        return self.name

x=3
print(x) #when we print a object by defaultt the str method call
print(x.__str__())
s=Student('maskur')
print(s)
print(s.__str__())