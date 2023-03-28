class Person:
    def __init__(self, person_name: str, age: int, height: str, person_id: int = None):
        # encapsulatioin
        self.__name = person_name  # double underscore used to define internal variable like private
        self.__age = age  # performing encapsulation . we can directly acces this variable outside of the class
        self.id = person_id  # public
        self.height = height

    def setName(self, newName):
        if self.__hasAnynumber__(newName):
            return
        self.__name = newName
    def getName(self):
        return self.__name
    def get_Age(self):
        return self.__age

    def __hasAnynumber__(self, string):
        if '0' in string:
            print('sorry name can not be a digit')
            return True
    #poly morphism in getSummary method
    def getSummary(self):
        pass


# inheritance
#student is a person
class Student(Person):
    def __init__(self,person_name,age,height,studnet_mail):
        super().__init__(person_name,age,height)
        #studnet has a email-> so attribute
        self.__email=studnet_mail

    #override the method getSummary()
    def getSummary(self):
        return f"Student {self.getName()},age is {self.get_Age()},email {self.__email}"
    def __str__(self):
        return self.getSummary()
class Teacher(Person):
    def __init__(self,name,age,height,dept):
        super().__init__(name,age,height)
        self.dept=dept
    def getSummary(self):
        return f"Teacher {self.getName()},Department: {self.dept}"

s=Student('maskur',20,'7ft','sabilhasan@gmail.com')
print(s.getSummary())
s.setName('maskur al shal sabil')
print(s.getSummary())
s2=Student('Humayun',22,'33inc','him@gmail.com')
print(s2)
teacher= Teacher('maskur',22,'3incs','ICT')
print(teacher.getSummary())