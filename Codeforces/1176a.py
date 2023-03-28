query=int(input())
while query:
    query-=1
    n=int(input())
    c=0
    while n!=1:
        if n%5==0: n= 4*n//5
        elif n%3==0: n=2*n//3
        elif n%2==0: n=n//2
        else :
            c=-1
            break
        c+=1
    print(c)