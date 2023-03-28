t=int(input())
while t:
    t-=1
    n,m=map(int,input().split())
    n=n-2
    m=m-2
    if n%3!=0:
        n=n//3+1
    else:
        n=n//3
    if m%3!=0:
        m=m//3 +1
    else:
        m=m//3
    print(n*m)