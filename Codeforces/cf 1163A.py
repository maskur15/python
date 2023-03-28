n,m=map(int,input().split())

d=n//2
if m==0:
    print(1)
elif m<=d:
    print(m)
else:
    print(n-m)

