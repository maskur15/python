n,m,k= map(int,input().split())
x = list(map(int,input().split()))
x1=[]
for i in range(n-1):
    x1.append(x[i+1]-x[i]-1)
x1.sort()

i=n-2
s=0
while True:
    if k == 1:
        break
    x[n-1]-=x1[i]
    k=k-1
    i-=1
print(x[n-1]-x[0]+1)


