def binaryPow(a,n,mod):
    if n==0:
        return 1
    if n==1:
        return  a
    if n%2==0:
        return  binaryPow((a*a)%mod,n//2,mod)%mod
    else:
        return  a*binaryPow((a*a)%mod,n//2,mod)%mod


if __name__=='__main__':
 while True:
    n= int(input())
    mod = 1000000007
    if n%2==0:
        ans1 = binaryPow(5,n//2,mod)
        ans2 = binaryPow(4,n//2,mod)
    else:
        ans1 = binaryPow(5,n//2+1,mod)
        ans2 = binaryPow(4,n//2,mod)
    print(ans1*ans2 % mod)
