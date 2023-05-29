#linked list using a tracking the last node  approach
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkdList:
    def __init__(self):
        self.head = None
        self.lastNode = None

    '''This one is a naive approach '''
    def insertNaive(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newnode
    '''A more updata by tracking the last node and set the next of that node '''
    def insert(self,data):
        'It will insert element in the list at the end '
        newnonde = Node(data)

        if self.head is None:
            self.head = newnonde
            self.lastNode  = newnonde
            return
        self.lastNode.next = newnonde
        self.lastNode = newnonde
    def showList(self):
        current =self.head
        while current:
            print(current.data)
            current=current.next

    def insertFront(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        self.head  = newnode
        self.head.next = temp


    def reverseLinkedList(self):
        rv = LinkdList()
        temp = self.head
        while temp:
            rv.insertFront(temp.data)
            temp=temp.next
        return rv
    def reverseList(self):
        if self.head is None:
            return
        current  = self.head.next
        if self.head:
            self.head = Node(self.head.data)
        while current is not None:
            temp = self.head
            self.head = Node(current.data)
            self.head.next= temp
            current=current.next
class Solution:
    def reverseList(self,head):
        if head is None:
            return
        newhead = Node(head.data)
        current = head.next
        while current :
            temp = newhead
            newhead = Node(current.data)
            newhead.next = temp
            current = current.next
        return newhead

def printList(head):
    temp = head
    while temp:
        print(temp.data,end=' ')
        temp = temp.next

if __name__ == '__main__':
    l =  LinkdList()
    l.insert(3)
    l.insert(34)
    l.insert(21)
    l.insert(11)
    l.insert(2)
    printList(l.head)

    print('Reverse a list')
    head = Solution().reverseList(head=l.head)
    printList(head)
  #  l.reverseList()


    print('complete')
