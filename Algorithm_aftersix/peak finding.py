print("peak finding ")
#find peak element in the array
def findPeak(arr,n):
    #first or last element is peak
    if n==1:
        return 0
    if arr[0]>=arr[1]:
        return 0
    if arr[n-1]>=arr[n-2]:
        return n-1
    #check for other element
    for i in range(1,n-1):
        #check if neighbors are smaller
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            return i
arr = [ 1, 3, 20, 4, 1, 0 ]
n=len(arr)
print("Index of a peak point is : ",findPeak(arr,n))
#this code is taken from: https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/