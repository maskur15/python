test = int(input())
while test :
    test -=1
    x,k = map(int,input().split())
    if x%k==0:
        print(2)
        print(x-1,1)
    else:
        print(f'1 \n {x}')
