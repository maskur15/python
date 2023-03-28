test =int(input())
while test:
    test-=1
    try:

        n=int(input())
        m=int(input())
        n-=1
        d=None
        while n:
            n-=1
            a=int(input())
            if d==None:
                d=m-a
            else:
                d=max(m-a,d)
            if a > m: m = a
        print(d)
    except Exception:
        break