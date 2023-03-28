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

    def get_Age(self):
        return self.__age

    def __hasAnynumber__(self, string):
        if '0' in string:
            print('sorry name can not be a digit')
            return True

    def getSummary(self):
        return (f"Nmae is {self.__name} age is : {self.__age}")


person_list = [Person('maskur', 22, '5inch', 3), Person('takbil', 29, '5inc'), Person('jadu', 22, '22inc', 2),
               Person('Dafaln', 49, '34inch', 3), Person('takbil', 20, '5inc'), Person('juiu', 11, '22inc', 2)]
for person in person_list:
    if person.get_Age()>=20:
        print(person.getSummary())