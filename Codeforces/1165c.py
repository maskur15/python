n=int(input())
x=list(input())
i=0
c=0
while i<n-1:
    if x[i]==x[i+1]:
        x[i]=''
        i=i+1
        c+=1
    else:
        i+=2
x=''.join(x)
if len(x)%2!=0:
    c+=1
    x=list(x)
    x[len(x)-1]=''
    x=''.join(x)
print(c)
print(x)
