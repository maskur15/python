from math import  sqrt
t=int(input())
while t:
    t-=1
    s=int(input())
    ans= (-1+sqrt(1-4*(-2*s)))//2
    print(int(ans))