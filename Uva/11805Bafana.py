t= int(input())
for i in range(t):
    t-=1
    n,k,p= map(int,input().split())
    d=n-k
    print('Case {}: '.format(i+1),end='')
    if p<=d:
        print(k+p)
    else:
        p=p-d
        p=p%n
        if p==0: print(n)
        else: print(p)
