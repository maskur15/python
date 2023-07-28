'''Design a class
-> insert a value(not duplicate)
-> get a rnadom value
-> remove  a element
'''
import random
class Store:
    def __init__(self):
        self.values = []
        self.isPreset={}
    def insert(self,val):
        if val in self.isPreset:
            return
        self.isPreset[val]=1
        self.values.append(val)
    def getvalue(self):
        return random.choice(self.values)
    def remove(self,val):
        if val in self.isPreset:
            del self.isPreset[val]
            self.values.remove(val)

if __name__ == '__main__':
    a=Store()
    a.insert(2)
    a.insert(3)
    a.insert(5)
    print(a.getvalue(),a.values)
    a.remove(3)
    print(a.getvalue(),a.values,a.isPreset)


