v={}
def isCorrect():
    res=list(v.keys())[0]
    value=v[res]
    f1=True

    f2=True
    c=0

    d=0
    f3=True
    for a in v:
        if v[a]==value:
            continue
        elif abs(value-v[a])==1:
            c+=1
        else:
            f2=False

        if v[a] == 1:
            continue
        else:
            f1 = False

        if v[a]==value:
            continue
        elif v[a]==1:
            d+=1
        else:
            f3=False
    if f1 or (f2 and c==1) or (f3 and d==1) or len(v)==1:
        return  True
    return False

n=int(input())
arr=list(map(int,input().split()))
for x in arr:
    if x in v:
        v[x]+=1
    else:
        v[x]=1

for i in range(n-1,-1,-1):
    if isCorrect():
        print(i+1)
        break
    else:
        v[arr[i]]-=1
        if v[arr[i]]==0:
            v.pop(arr[i])

