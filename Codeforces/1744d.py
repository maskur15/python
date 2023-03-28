##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
# BY-GK
from math import log2
from math import sqrt
def mergeSort(arr):
    if len(arr)==1:
        return arr
    ind=len(arr)//2
    left=arr[:ind]
    right=arr[ind:]
    mergeSort(left)
    mergeSort(right)
    i=k=j=0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]; j+=1 ; k+=1
    while i<len(left):
        arr[k]=left[i]
        k+=1;i+=1
    while j<len(right):
        arr[k]=right[j]
        k+=1; j+=1
    return arr

def multix(n):
    if log2(n)==int(log2(n)):
        return n
    i=2
    ans=1
    ln=int(log2(n))
    for _ in range(1,ln+1):
        if n%i==0:
            ans=max(ans,i)
            if log2(n//i)==int(log2(n//i)):
                ans=max(ans,n//i)
        i=i*2
    return ans

if __name__ == '__main__':
    ps = list()
    d=dict()
    for i in range(1,200001):
        v=int(log2(multix(i)))
        ps.append(v)
        d[i]=v

    test=int(input())
    while test:
        test-=1
        n=int(input())
        ar=list(map(int,input().split()))
        ans=0
        for v in ar:
            if v not in d:
                c=log2(multix(v))
                d[v]=int(c)
            ans+=d[v]
        i=0
        sr=ps[:n]
        mergeSort(sr)
        while i<n:
            if ans>=n or sr[i]==0:
                break
            ans+=sr[i]
            i+=1
        if ans>=n:
            print(i)
        else:print(-1)


# That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.