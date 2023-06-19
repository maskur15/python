def binarySearch(ar,left,right,num):
    if left>right:
        return -1
    mid = (left+right)//2
    if ar[mid]==num:
        return mid
    if ar[mid]>num:
        return binarySearch(ar,left,mid-1,num)
    return binarySearch(ar,mid+1,right,num)
if __name__ == '__main__':
    ar=[2,3,5,9,10]
    print(binarySearch(ar,0,len(ar)-1,49))