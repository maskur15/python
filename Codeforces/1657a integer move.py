import math
t=int(input())
while t:
    t-=1
    x,y=map(int,input().split())
    v=math.sqrt(x*x+y*y)
    if x==0 and y==0:
        print(0)
        continue
    if v==int(v):
        print(1)
        continue
    print(2)
