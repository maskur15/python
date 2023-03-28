#each ith iteration find the ith minimum element and put it ith index

def selectionSort(arr):
    for i in range(0,len(arr)):
        index=i
        for j in range(i+1,len(arr)):
            if arr[index]> arr[j]:
                index=j
        temp=arr[i]
        arr[i]=arr[index]
        arr[index]=temp
    return arr
arr = list(map(int,input().split()))
print(arr)
print(selectionSort(arr))