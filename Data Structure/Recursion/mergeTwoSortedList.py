class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,data):
        node = Node(data)
        if self.head is None:
            self.head= node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def show(head):
    if head:
        print(head.data,end=' ')
        return show(head.next)
    print()
def mergeSortedList(head1,head2):
    if head1 is None: return head2
    if head2 is None: return head1
    if head1.data < head2.data:
        head1.next = mergeSortedList(head1.next,head2)
        return  head1
    else:
        head2.next = mergeSortedList(head1,head2.next)
        return head2

if __name__ == '__main__':
    l  = LinkedList()
    l2 = LinkedList()

    ar = [1,2,5,6]
    ar2= [2,3,4]
    for a in ar:
        l.insert(a)
    for a in ar2:
        l2.insert(a)
    show(l.head)
    show(l2.head)
    head = mergeSortedList(l.head,l2.head)
    print('merge list : ')
    (show(head))
