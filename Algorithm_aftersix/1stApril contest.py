n=int(input())
while n:
    n-=1
    r,c=map(int,input().split())
    x=""
    for i in range(250):
        x+='RD'
    x+='LLUU'
    print(len(x))
    print(x)