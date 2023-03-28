#building max heap using array

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
    if l<len(heap) and heap[l]>heap[largest]:
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
if __name__=='__main__':
    arr=[2,1,4,5,9,10,7,22,99,19,101]
    print(arr)
    build_maxHeap(arr)
    print(arr)
