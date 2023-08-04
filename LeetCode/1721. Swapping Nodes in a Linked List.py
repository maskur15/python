class ListNode:
    def __init__(self,val):
        self.val=val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,val):
        node = ListNode(val)
        if self.head==None:
            self.head=self.tail=node
        else:
            self.tail.next=node
            self.tail=node
def show(head):
    if head:
        print(head.val,end=' ')
        show(head.next)
def swapNode(head,k):
    #swap the kth node from both side
    fast=slow=head
    for _ in range(k):
        fast=fast.next
    while fast:
        fast=fast.next
        slow=slow.next
    #now the slow has the node which is the kth node from the end
    #now get the kth node from begning and swap the value
    temp=head
    for _ in range(k-1):
        temp=temp.next
    val=temp.val
    temp.val=slow.val
    slow.val=val
    return  head
if __name__ == '__main__':
    l=LinkedList()
    for _ in range(11):
        l.insert(_)
    show(l.head)
    head = swapNode(l.head,6)
    print()
    show(head)
