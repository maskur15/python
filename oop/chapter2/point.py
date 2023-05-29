from oop import addObjectinLIst
class Point:
    def reset(self):
        self.x =0
        self.y = 0
p1 = Point()
p2 = Point()
p1.x = 4

print(p1.x)
p1.reset()
print(p1.x)
print(p1.y)
p = addObjectinLIst.Person('maskur',4,'3',3)
print(p.getSummary())