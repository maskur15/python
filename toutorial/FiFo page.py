from  queue import  Queue
def Fifo(pageref,n,num_pageframe):
    s = set()
    page_q = Queue()
    miss =0
    for i in range(n):
        if len(s)<num_pageframe:
            if pageref[i] not in s:
                miss+=1
                s.add(pageref[i])
                page_q.put(pageref[i])
        else:
            if pageref[i] not in s:
                miss+=1
                s.remove(page_q.get())
                s.add(pageref[i])
                page_q.put(pageref[i])
    return miss
if __name__=='__main__':
    pages=[7,0,1,2,0,3,0,4,2,3,0,3,2]
    n=len(pages)
    capacity = 4
    print(Fifo(pages,n,capacity))