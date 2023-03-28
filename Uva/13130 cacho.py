t = int(input())
while t:
    t-=1
    ar=list(map(int,input().split()))
    f=False
    for i in range(1,5):
        if ar[i]-1==ar[i-1]:
            continue
        else:
            f=True
    if f: print('N')
    else:print('Y')