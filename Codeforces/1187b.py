n = int(input())
x = input()
m = int(input())
d1={}
dc={}
k=0
for c in x:
    k+=1
    if c in dc:
        dc[c]+=1
    else:dc[c]=1

    t=(c,dc[c])
    d1[t]=k
while m:
    m -= 1
    d2={}
    s=input()
    for c in s:
        if c in d2: d2[c]+=1
        else: d2[c]=1
    ans=0
    for v in d2:
        if ans < d1[(v,d2[v])]:
            ans=d1[(v,d2[v])]
    print(ans)



