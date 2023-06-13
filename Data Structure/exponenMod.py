def binaryPow(a,n,mod):
    if n==0:
        return 1
    if n==1:
        return  a%mod
    if n%2==0:
        return  binaryPow((a*a)%mod,n//2,mod)%mod
    else:
        return  a*binaryPow((a*a)%mod,n//2,mod)%mod
while True:
    a,n = map(int,input().split())
    print(binaryPow(a,n,10000000))