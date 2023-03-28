class Person:
    def __init__(self,person_name:str,age:int,person_id:int=None):
        #encapsulatioin
        self.__name=person_name # double underscore used to define internal variable like private
        self.__age=age #performing encapsulation . we can directly acces this variable outside of the class
        self.id=person_id  #public
    def setName(self,newName):
        if self.__hasAnynumber__(newName):
            return
        self.__name=newName

    def __hasAnynumber__(self,string):
        if '0' in string:
            print('sorry name can not be a digit')
            return True
    def getSummary(self):
        print( f"Nmae is {self.__name} age is : {self.__age}")


person1=Person('hasan',39)

person1.getSummary()
person1.setName('sabil hasan')
person1.getSummary()
person1.setName('0202xjfha')
person1.getSummary()
print(person1.id)
person2=Person('jamaila',22,3)
person2.getSummary()