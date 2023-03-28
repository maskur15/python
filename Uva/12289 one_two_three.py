n=int(input())
while n:
    n-=1
    x=input()
    if len(x)==3:
        if (x[0]=='t'and x[1]=='w') or (x[0]=='t' and x[2]=='o') or (x[1]=='w' and x[2]=='o'):
            print(2)
        else:
            print(1)
    else:
        print(3)