t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    s=1
    c=0
    while True:
        if s>=n:
            break
        c+=1

        s+=min(s,k)
    print(c)