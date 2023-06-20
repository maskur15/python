def mergeSort(ar):
    if len(ar)==1:
        return ar
    mid = len(ar)//2
    left_arr = ar[:mid]
    right_arr = ar[mid:]
    ar1 = mergeSort(left_arr)
    ar2 = mergeSort(right_arr)
    print(ar1," <> ",ar2)
    return merge(ar1,ar2)
   # return merge(ar,ar1,ar2) #passing the array will mdify the original array

def merge(left_arr,right_arr):
    i=j=k=0
    ar=[0]*(len(left_arr)+len(right_arr))
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<right_arr[j]:
            ar[k]=left_arr[i]
            k+=1; i+=1
        else:
            ar[k]= right_arr[j]
            k+=1 ; j+=1
    while i<len(left_arr):
        ar[k] = left_arr[i]
        k += 1
        i += 1
    while j<len(right_arr):
        ar[k] = right_arr[j]
        k += 1
        j += 1
    return ar
if __name__ == '__main__':
    ar = [6,2,3,5,1,7,9,8]
    print(mergeSort(ar))
    print(ar)