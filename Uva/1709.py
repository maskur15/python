from math import sin
from math import  cos
def price(k,p,a,b,c,d):
    return p*(sin(a*k+b)+cos(c*k+d)+2)
while True:
    try:
        p,a,b,c,d,n=map(int,input().split())
        ar=list()
        diff=0
        for i in range(1,n+1):
            ar.append(price(i,p,a,b,c,d))
        m=ar[0]
        for i in range(1,n):
            if ar[i]>m : m=ar[i]
            else:
                diff=max(diff,m-ar[i])
        print('%.4f'%diff)
    except Exception:
        break
