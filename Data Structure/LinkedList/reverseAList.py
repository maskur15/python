class TreeNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,val):
        node=TreeNode(val)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
def show(head):
    while head:
        print(head.val)
        head=head.next
def insert(tail,val):
    tail.next=TreeNode(val)
    tail=tail.next
    return tail
def reverse(head):
    rev=head
    head=head.next #first change the head node then make the rev.next none otherwise it will change the head
    rev.next=None
    while head:
        t=head
        head=head.next
        t.next=rev
        rev=t
    return rev
if __name__ == '__main__':
    head=TreeNode(1)
    tail=head
    for i in range(2,10):
        tail=insert(tail,i)
    show(head)
    rev=reverse(head)
    show(rev)
