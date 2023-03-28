n,v = map(int,input().split())
n=n-1
i=2
if v>=n:
    print(n)
    exit()
c=v
while i:
     if v>=n:
         break
     n=n-1
     c=c+i
     i=i+1
print(c)

