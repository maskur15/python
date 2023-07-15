def merge_sort(nums):
    n= len(nums)
    if n==1:
        return nums
    left = nums[:n//2]
    right = nums[n//2:]
    ar1= merge_sort(left)
    ar2= merge_sort(right)
    i=0
    j=0
    k=0
    while i<len(ar1) and j<len(ar2):
        if ar1[i] < ar2[j]:
            nums[k] = ar1[i]
            i+=1
            k+=1
        else:
            nums[k]=ar2[j]
            j+=1
            k+=1
    while i < len(ar1) :
            nums[k] = ar1[i]
            i += 1
            k += 1
    while j < len(ar2):
            nums[k] = ar2[j]
            j += 1
            k += 1
    return nums
if __name__ == '__main__':
    ar = [1,3,1,5,2]
    print(merge_sort(ar))