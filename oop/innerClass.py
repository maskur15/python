class Student:
    def __init__(self,name):
        self.name=name
        self.lap=Student.Laptop()

    class Laptop:
        def __init__(self):
            self.brand='hp'
            self.core='i5'

        def show(self):
            print(self.brand,self.core)
s=Student('amskur')
b=s.Laptop()
print(b.core,b.brand)
print(s.lap)
s.lap.show()