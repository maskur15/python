
def findStep(arr,q):
    l=0
    r=len(arr)-1
    while l<=r:
        ind=(l+r)//2
        if arr[ind]==q:
            return ind
        if arr[ind]>q:
            r=ind-1
        if arr[ind]<q:
            l=ind+1
    return 'not found'
if __name__ == '__main__':
    ar=[2,4,5,3,2,5,6,99,22,32,20]
    ar.sort()
    print(findStep(ar,6))