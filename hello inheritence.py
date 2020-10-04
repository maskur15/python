#inheritence in python
class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color= color
        print("Init method invoke")
    def AnimalBark(self):
        print("Animal Barking..!!!")
class Cat(Animal):
    def purr(self):
        print("purr.......")
    def bark(self):
        super().AnimalBark()
        print("MEw mew Mew...")

class Dog(Cat):
    def bark(self):
        print(self.name,": : Ghew Ghew .....")
fido = Dog("FIdod","brown")
zigri=Cat("zigri","dark")
zigri.purr()
fido.bark()
zigri.bark()