t=int(input())
while t:
    t-=1
    n=int(input())
    x=list(map(int,input().split()))
    x.sort()

    for i in range(n-1):
        if x[i+1]-x[i]>1:
            print("NO")
            break
    else:
     print("YES")