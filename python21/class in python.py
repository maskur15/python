class man:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name +" is " +str(self.age)
    def birhtday(self):
        print('Happy birthday you were',self.age)
        self.age+=1
        print('You were ',self.age)
    def isAdult(self,baseage):
        if self.age>=baseage:
            return 'adult'
        else:
            return 'not adult'
m=man('maskur',20)
print(m)
