class person:
    instance_count=0
    @classmethod
    def increment(cls):
        cls.instance_count+=1
    def __init__(self,name,age):
        self.name=name
        self.age=age
        person.increment()
    def getdata(self):
        return  self.name +' age is '+str(self.age)
    def setHobby(self,hobby):
        self.hobby=hobby
    def getHobby(self):
        return self.hobby
    def __str__(self):
        return self.name+' is '+str(self.age)
    def __fight__(self):
        print('git fight fight')
p1 = person('hasan',39)
p2 =person('manik',32)
p1.setHobby('typing')
print(p1.getdata())
"""
print("class attributes")
print(person.__name__)
print(person.__module__)
print(person.__doc__)
print(person.__dict__)
print(p1.__class__)
print(p1.__dict__)

"""