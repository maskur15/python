from queue import  Queue
def FIFO(ref_num,n,pageframe):
    miss=0
    s=set()
    q=Queue()
    for i in range(n):
        if ref_num[i] not in s:
            miss+=1
            if len(s)<pageFrame:
                s.add(ref_num[i])
                q.put(ref_num[i])
            else:
                s.remove(q.get())
                s.add(ref_num[i])
                q.put(ref_num[i])


    return miss
print("Enter the number of pgae reference : ")
n=(int)(input())
print("Enter the page reference : ")
arr = map(int, input().split())
ref_num = list(arr)
print("Enter the number of frame  : ")
pageFrame = (int)(input())
print("Number of page fault : ",FIFO(ref_num,n,pageFrame))

