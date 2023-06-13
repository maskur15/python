def binaryPow(a,n):
    if n==0:
        return 1
    if n==1:
        return  a
    if n%2==0:
        return  binaryPow(a*a,n//2)
    else:
        return  a*binaryPow(a*a,n//2)
while True:
    a,n = map(int,input().split())
    print(binaryPow(a,n))