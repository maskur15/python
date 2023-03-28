#max-heap build, insert ,delete

def insert(ar,num):
    ar.append(num)
    parentHeapify(ar,len(ar)-1)
#parent heapify when new value inserted
def parentHeapify(ar,i):
    p=(i-1)//2
    if p>=0 and  ar[i]>ar[p]:
        temp=ar[p]
        ar[p]=ar[i]
        ar[i]=temp
        parentHeapify(ar,p)
#delete the root which is max element
#removing the last element and put it in the root  then again heapyify the array
def delete(ar):
    ar[0]=ar[len(ar)-1]
    ar.pop()
    heapify(ar,0)

#max heapify
def heapify(ar,i):
    index=i
    l=i*2+1 #left child
    r=i*2+2 #right child
    if l<len(ar) and ar[l]> ar[index]:
        index=l
    if r<len(ar) and ar[r]>ar[index]:
        index=r

    if index!=i :
        temp=ar[i]
        ar[i]=ar[index]
        ar[index]=temp
        heapify(ar,index)
#call this method to convert a list to a max heap
def buildHeap(ar):
    n=len(ar)
    for i in range(len(ar)//2-1,-1,-1):
        heapify(ar,i)
if __name__=='__main__':
    arr = [10, 5, 3, 2, 4, 1, 7]
    buildHeap(arr)
    print(arr)
    insert(arr,22)
    insert(arr,-33)
    print(arr)
    insert(arr,4)
    print(arr)
    delete(arr)
    print(arr)
    delete(arr)
    print(arr)
    delete(arr)
    print(arr)