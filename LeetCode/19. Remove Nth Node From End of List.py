class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next = None
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

def removeNthNode(head,n):
    first=head
    second=head
    while n:
        second=second.next
        n-=1
    if second==None:
        return first.next

    while second.next:
        second=second.next
        first=first.next
    first.next=first.next.next
    return head

if __name__ == '__main__':
    l=LinkedList()
    for i in range(5):
        l.insert(i)
    show(head=l.head)
    head=removeNthNode(l.head,1)
    show(head)