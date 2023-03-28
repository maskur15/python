ar=list()
for i in range(1,10):
    ar.append(str(i)+'m')
    ar.append(str(i)+'p')
    ar.append(str(i)+'s')
ar.sort()
x=list(input().split())
ans=33
for a in ar:
    c=0
    if x[0]!=a  : c+=1
    if x[1]!=a: c+=1
    if x[2]!=a: c+=1
    ans=min(c,ans)
x.sort()
for i in range(len(ar)-6):
    #print(i,':',ar[i],ar[i+3],ar[i+6])
    c=0
    if x[0]!=ar[i]: c+=1
    if x[1]!=ar[i+3]: c+=1
    if x[2]!=ar[i+6]: c+=1
    ans=min(c,ans)
print(ans)

