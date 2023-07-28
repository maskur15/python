class Student:
    def __init__(self):
        pass
    '''overloading usingthe tehnique None '''
    @staticmethod
    def sum(x=None,y=None,z=None):
        if x and y and z :
             print(x+y+z)
        elif x and y:
            print(x+y)
        else:print(x)
    '''overlaoding using varible len args k*'''
    @staticmethod
    def avg(*var):
        s=0
        for v in var:
            s+=v
        if len(var)==0:
            print(0)
        else:
           print(s/len(var))

s=Student()
s.sum(2,3)
s.sum(3)
s.sum(3,5,6)
s.avg()
s.avg(2,3,5)