#https://codeforces.com/contest/1166/problem/A

from math import comb
n=int(input())
d=dict()
while n:
    n-=1
    x=input()
    if x[0] in d:
        d[x[0]]+=1
    else:
        d[x[0]]=1

s=0
for v in  d:
    if d[v]>=3:
       x= d[v]//2
       y=x+ d[v]%2
       if x>=2:
           s+= comb(x,2)
       if y>=2:
           s+= comb(y,2)

print(s)

