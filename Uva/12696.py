test=int(input())
c=0
while test:
    test-=1
    length,width,depth,weight=map(float,input().split())
    if ((length<=56 and width<=45 and depth<=25 )or (length+width+depth)<=125) and weight<=7:
        print(1)
        c+=1
    else:print(0)
print(c)