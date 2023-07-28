'use hare and tortoise one pointer move one step anotehr move two step'
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail = None
    def insert(self,val):
        node=ListNode(val)
        if self.head==None:
            self.head=node
            self.tail=node
            return
        self.tail.next=node
        self.tail=node
    def show(self):
        while self.head:
            print(self.head.val)
            self.head=self.head.next
def printList(head):
    while head:
        print(head.val,end=' ')
        head=head.next
def getMiddleNode(head):
    firstNode=head
    lastNode=head
    while lastNode and lastNode.next:
        lastNode=lastNode.next.next
        firstNode=firstNode.next
    return firstNode
if __name__ == '__main__':
    l=LinkedList()
    l.insert(5)
    l.insert(6)

   #l.show()
    node=getMiddleNode(l.head)
    printList(node)
