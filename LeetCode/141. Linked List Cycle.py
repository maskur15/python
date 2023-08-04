class ListNode:
    def __init__(self, val:int=0, next=None):
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
def isCycle(head):
    if head==None:
        return False
    if head and head.next==None:
        return False
    first=head
    second=head.next.next
    while second:
        print(second.val,first.val)
        if first==second:

            return True
        second=second.next.next
        first=first.next

    return False

def show(head):
    if head:
        print(head.val,end=' ')
        show(head.next)

if __name__ == '__main__':
    first = ListNode(2)
    head=first
    first.next=first
    print(isCycle(head))
