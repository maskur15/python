#http://rosalind.info/problems/fib/
n,m=map(int,input().split())
p0=1
p1=0
c0=0
c1=0
for i in range(n-1):
    c0=p1*m
    c1=p1+p0
    p0=c0
    p1=c1
print(p0+p1)