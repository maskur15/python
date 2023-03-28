def g(n):
    s=0
    while n>=1:
        s=s+n%10
        n=n//10
    if s//10==0:
        return s
    return g(s)
while True:
    n=int(input())
    if n==0: break
    print(g(n))
