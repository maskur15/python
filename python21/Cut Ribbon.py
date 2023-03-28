n,a,b,c=map(int,input().split())
ans=0
for i in range(n+1):
    for j in range(n+1):
        x= int((n-b*i - c*j)/a)
        if x*a+i*b+j*c==n and x>=0:
            ans=(max(x+i+j,ans))
print(ans)