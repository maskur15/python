t =int(input())
while t:
    t-=1
    n = int(input())
    x = list(map(int,input().split()))
    i=0
    f= True
    while i<n:
        if f:
            print(x[i],end=" ");
            f= False
            i=i+1
        else:
            print(x[n-1],end=" ");
            n=n-1
            f= True
    print()