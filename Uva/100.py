def anti(n,c):
    c+=1
    if n==1 : return c
    if n%2==0: return anti(n//2,c)
    else: return  anti(3*n+1,c)
while True:
    a,b=map(int,input().split())
    ans=0
    for i in range(a,b+1):
        ans=max(ans,(anti(i,0)))
    print(a,b,ans)
