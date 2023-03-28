# each iteration put the element in its right place

def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp
            else:
                break
    return  arr
arr =list(map(int,input().split()))
print(insertionSort(arr))
