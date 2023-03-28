t = int(input())
while t>=1:
    n = int(input())
    x = list(map(int,input().split()))
    x.sort()
    c=0
    for a in x:
       c+=a
    if c==0:
        print("NO")
    elif c>0:
        x.reverse()
        print("YES")
        for a in x:
            print(a," ",end="")
        print()
    else:
        print("YES")
        for a in x :
            print(a," ",end="")
        print()

    t=t-1

