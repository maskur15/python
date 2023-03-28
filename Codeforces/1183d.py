q=int(input())
while q:
    q-=1
    n=int(input())
    arr=list(map(int,input().split()))
    d=[0]*(n+1)
    for a in arr:
        d[a-1]+=1
    d.sort(reverse=True)
    s=d[0]
    v=s
    for i in range(1,n):
        v=min(v-1,d[i])
        s+=v
        if v==0:
            break
    print(s)