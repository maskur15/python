class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head:[ListNode]):
        pass
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,val):
        node=ListNode(val)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
def show(head):
    if head:
        print(head.val,end=' ')
        show(head.next)
def swapUsingRecursion(head):
    if head==None :
        return
    if head.next==None:
        return head
    if head and head.next:
        temp=head.next
        head.next=head.next.next
        temp.next=head
        head=temp
        head.next.next=swapUsingRecursion(head.next.next)
        return head


def swap(head):
    ar=[]
    ar2=[]
    temp=head
    while temp and temp.next:
        ar2.append(temp)
        ar.append(temp.next)
        temp=temp.next.next
    if temp:
        ar2.append(temp)
    if ar:
        tail =ar.pop(0)
        head=tail
        f=True
        while ar and ar2:
            if f:
                tail.next=ar2.pop(0)
                tail=tail.next
                f=False
            else:
                tail.next=ar.pop(0)
                tail=tail.next
                f=True
        while ar:
            tail.next=ar.pop(0)
            tail=tail.next
        while ar2:
            tail.next=ar2.pop(0)
            tail=tail.next
        if tail:
            tail.next=None
        return head
    else:
        return head


if __name__ == '__main__':
    l=LinkedList()
    for i in range(1,8):
        l.insert(i)
    head=swapUsingRecursion(l.head)
    show(head)