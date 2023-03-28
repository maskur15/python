n=int(input())
x=list(map(int,input().split()))
m=max(x)+1
ans=[0]*m
for a in x:
    ans[a]+=1
for i in range(2,m):
    ans[i]=max(ans[i-1],ans[i-2]+ans[i]*i)
print(max(ans))