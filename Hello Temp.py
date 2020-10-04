t =int(input())
while t>0:
    t-=1
    n = int(input())
    if n%2==0:
        print(int(n/2)-1)
    else:
        print(int(n/2))