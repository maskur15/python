n=int(input())
x =(input())
s=0
for  a in x:
    s+= int(a)
for i in range (2,n+1):
    t=i
    if s%i==0:
       s1=0; d=s/i;
       for a in x:
           s1+=int(a)
           if s1>d:
               break
           elif s1==d:
               t-=1
               s1=0
    if t==0:
        print("YES")
        exit()
print("NO")



