t=int(input())
while t:
   t=t-1
   n=int(input())
   x=list(map(int,input().split()))
   f=x[0]
   if x.count(f)==n:
       print('-1')
   else:
       f=False;f1=False
       for  i in range(n):
           if x[i]==max(x):
               f=True
               ans=i
           elif f:
               print(ans+1)
               break
           if x[i] != max(x):
               f1=True
           elif f1:
               print(i+1)
               break




