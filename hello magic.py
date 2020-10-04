#magic method in python
print("python magic method")
class Vector2D:
     def __init__(self,x,y):
        self.x=x
        self.y=y
     def __add__(self, other):
        return Vector2D(self.x+other.x,self.y+other.y)
class String:
    def __init__(self,content):
        self.content=content
    def __truediv__(self, other):
        return String(self.content+other.content)
first = Vector2D(2,4)
second=Vector2D(3,5)
Third = first+second
print(Third.x,Third.y)
string1= String("Maskur al")
string2=String(" Shal sabil")
result= string1/string2
print(result.content)
#list of magic method are given below
#__sub__ for -
#__mul__ for *
#__truediv__for/
#floordiv for //
# __mod__  for %
#__pow__ for **
#__and__ for &
# __xor__for ^
# __or__ for |
