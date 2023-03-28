n=int(input())
arr=list(input().split())
ans=arr[0]
for k in range(1,len(arr)):
    w=arr[k]
    l1= len(ans)
    l2=len(w)
    if l1>=l2:
        i=l1-l2
    else:
        i=0
    j=0
    while i <l1:

        if ans[i]==w[j]:
            j+=1
            i=i+1
            continue
        elif i==l1-1 and ans[i]==w[0]:
            j=1
            i+=1
        else:
            i=i+1
            j=0
    ans+=w[j:]

print(ans)