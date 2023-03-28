t=int(input())
while t:
    t-=1
    a=list(map(int,input().split()))
    y='Y'
    for i in range(4):
        if a[i]+1==a[i+1]:
            continue
        else: y='N'
    print(y)