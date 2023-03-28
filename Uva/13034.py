t=int(input())
for i in range(1,t+1):
    a=list(map(int,input().split()))
    y="Yes"
    for x in a:
        if x==0:
            y="No"
    print('Set #{}: {}'.format(i,y))
