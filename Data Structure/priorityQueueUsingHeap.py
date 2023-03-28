#priority queue using max heap

def leftCHild(i):
    return i*2+1
def rightChild(i):
    return i*2+2
def parent(i):
    return (i-1)//2

def max_heapify(heap,i):

    l= leftCHild(i)
    r= rightChild(i)
    largest=i
    if l<len(heap) and heap[l]>heap[i]:
        largest=l
    if r<len(heap) and heap[r]>heap[largest]:
        largest=r
    if largest!=i:
        t=heap[i]
        heap[i]=heap[largest]
        heap[largest]=t
        max_heapify(heap,largest)
def build_maxHeap(arr):
    for i in range((len(arr)-1)//2,-1,-1):
        max_heapify(arr,i)
def extractTop(arr):
    top=arr[0] #first element of the array is the mx value
    arr[0]=arr[len(arr)-1] #change the first element with last element
    arr.pop() #remove the last element
    max_heapify(arr,0)
    return  top

def insertValue(arr,v):
    if len(arr)==0:
        arr.append(v)
    else:

        i=len(arr)
        arr.append(v)
        #while i not the parent node 0
        while i>=1 and  arr[i]>arr[parent(i)]:
            t= arr[i]
            arr[i] = arr[parent(i)]
            arr[parent(i)]=t
            i= parent(i)


if __name__=='__main__':
    arr=list()
    insertValue(arr,4)
    print(arr)
    insertValue(arr,44)
    insertValue(arr,33)
    insertValue(arr,12)
    print(arr)
    print(extractTop(arr))
    print(arr)
