import math
class Point:
    def move(self,x,y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(0,0)
    def calculate_distance(self,otherPoint):
        return math.sqrt((self.x-otherPoint.x)**2 + (self.y-otherPoint.y)**2)
p1= Point()
p2 = Point()
p1.reset()
p2.reset()
p2.move(5,0)
print(p2.calculate_distance(p1))
p1.move(2,3)
print(p2.calculate_distance(p1))