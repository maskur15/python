class TreeNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
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
root=None
def getlen(head):
    temp=head
    c=0
    while temp:
        c+=1
        temp=temp.next
    return c
def reorder(head):
    ar=[]
    temp=head
    while temp:
        ar.append(temp)
        temp=temp.next
    i=1
    j=len(ar)-1
    f=True
    head=ar[0]
    tail=ar[0]
    while i<=j:
        if f:
            tail.next=ar[j]
            j-=1
            tail=tail.next
            f=False
        else:
            tail.next=ar[i]
            i+=1
            tail=tail.next
            f=True
    if tail:
        tail.next=None
    show(head)

if __name__ == '__main__':
    head=TreeNode(1)
    tail=head
    for i in range(2,7):
        tail=insert(tail,i)
    reorder(head)

