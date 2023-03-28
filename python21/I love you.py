n=int(input())
x=list(map(int,input().split()))
m1=x[0]
m2=x[0]
c=0
for i in range(1,n):
     if m1<x[i]:
         c+=1
         m1=x[i]
     elif m2> x[i]:
         c+=1
         m2=x[i]
print(c)