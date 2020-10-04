#class in python
class cat:
    #__init__(object,value)
    def __init__(self,color,name):
        self.color=color
        self.name=name
        print("init")
    def display(self):
        print(self.color,self.name)
felix = cat("red","JOny")
rovy=cat("black","SUnny")
felix.display()
rovy.display()