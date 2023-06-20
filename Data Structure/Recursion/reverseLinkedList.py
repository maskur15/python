class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def showList(head):
    temp =head
    while temp:
        print(temp.data,end=' ')
        temp=temp.next
#reverse using recursion
def reverse(head:Node):
    if head is None or head.next is None:
        return head
    final_head  = reverse(head.next)
    head.next.next = head
    head.next = None
    return  final_head
#reverse iterative
def reverse_linkedlist(head):
   rev_head = None
   while head:
       temp = head.next
       head.next = rev_head
       rev_head = head
       head = temp
   return rev_head



if __name__ == '__main__':
     l = LinkedList()
     ar =[2,3,4,6]
     for a in ar:
         l.insert(a)
     showList(l.head)
     head = reverse(l.head)
     print('\nreveerse: ')
     showList(head)
     print()
     reverse_linkedlist(head)
