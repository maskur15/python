from decimal import *
getcontext().prec=2
def love(x):
    a=0
    for v in x:
        if v.isalpha():

            if v >= 'A'and v  <=('Z'):

                a += ord(v) - ord('A') + 1
            else:
                a += ord(v)- ord('a') + 1
    return a
def g(n):
    s=0
    while n>=1:
        s=s+n%10
        n=n//10
    if s//10==0:
        return s
    return g(s)
while True:
    try:
        x=input()
        y=input()
        a=g(love(x))
        b=g(love(y))
        if a>b:
            print('%.2f'%(b/a*100),'%')
        else:print('%.2f'%(a/b*100),'%')

    except Exception:

        break