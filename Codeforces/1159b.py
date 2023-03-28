n=int(input())
x=list(map(int,input().split()))
ans=9999999999
for i in range(n):
    l= max(i,n-i-1)

    ans=min(ans,x[i]//l)
print(ans)