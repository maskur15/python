t=int(input())
print('Lumberjacks:')
while t:
    t-=1
    ar=list(map(int,input().split()))
    ff= True
    f=True
    for i in range(1,len(ar)):
        if ar[i-1]>ar[i]:
            ff=False
        if ar[i]>ar[i-1]:
            f=False

    if f or ff: print('Ordered')
    else: print('Unordered')