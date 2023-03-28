t=int(input())
while t:
    t=t-1
    n,l,r= map(int,input().split())
    arr=list(map(int,input().split()))
    ans=0
    for i in range(n-1):
        for j in range(i+1,n):
            num=arr[i]+arr[j]
            if num>=l and num<=r:
                ans+=1
    print(ans)
