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
        if left[i]<right[j]:
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

if __name__=='__main__':
    arr=[6,5,12,10,9,1]
    mergeSort(arr)
    print(arr)