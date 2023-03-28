n,m=map(int,input().split())
x=list(map(int,input().split()))
c=0
arr=[0]*(n+1)
for i in range(m):
    if arr[x[i]]==0:
        c+=1
    arr[x[i]]+=1
    if c==n:
        print('1',end='')
        for k in range(1,n+1):
            arr[k]-=1
            if arr[k]==0:
                c-=1
    else:
        print('0',end='')
