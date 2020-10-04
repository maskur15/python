#Python program to demmonstrate class method and static method
from datetime import date
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #class method to create a person object by birth year
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)
    #static method to check if a person is adult or not
    @staticmethod
    def isAdult(age):
        return age>18

person1 = Person("Mandi",14)
person2= Person.fromBirthYear("Zabria",1999)
print(person1.age)
print(person2.age)
print(person1.isAdult(person1.age))

# function  can be called without creating  any object
print("FUnction....... ")
def isMature(age):
    return age > 18
print(isMature(89))