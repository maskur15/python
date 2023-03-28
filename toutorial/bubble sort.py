def bubbleSort(arr):
    f=True
    for i in range(1,len(arr)):
        f=True
        for j in range(len(arr)-i):
            if arr[j]> arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                f=False
        if f:
            break
    return arr

arr= list(map(int,input().split()))
print(arr)
print("sorted :",bubbleSort(arr))