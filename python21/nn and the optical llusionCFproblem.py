import  math
n,R=map(int,input().split())
print(R*(math.sin(math.radians(180/n))) / (1 -math.sin(math.radians(180/n))))
