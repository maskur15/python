n,l=map(int,input().split())
x=set(map(int,input().split()))
x=list(x)
x.sort()
m=-1
for i in range(1,len(x)):
     m=max(m,x[i]-x[i-1])
m=m/2
if x[0]!=0 and m<x[0]:
    m=x[0]
if x[len(x)-1]!=l and m< l-x[len(x)-1] :
    m=l-x[len(x)-1]
print(m)
#46  615683844