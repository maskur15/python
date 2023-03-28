#peak finding using binary search
def findPeak(arr,low,high,n):
    mid=int((low+high)/2)
    if mid==n-1:
        return mid
    if mid==0 and arr[mid]>=arr[mid+1]:
        return mid
    if mid==n-1 and arr[mid]>=arr[mid-1]:
        return mid
    if arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]:
        return mid
    elif mid>0 and arr[mid-1]>arr[mid]:
        return  findPeak(arr,low,mid-1,n)
    else:
        return  findPeak(arr,mid+1,high,n)
arr=[1,3,20,4,1,0]
n=len(arr)
print("Index of a peak point is : ",findPeak(arr,0,n-1,n))