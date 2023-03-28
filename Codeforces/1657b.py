t=int(input())
while t:
    t-=1
    n,b,x,y=map(int,input().split())
    sum=0
    value=0
    for i in range(n):
        if value+x<=b:
            value=value+x
        else :
            value=value-y
        sum+=value
    print(sum)