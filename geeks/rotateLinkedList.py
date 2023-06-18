class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def show(head):
    while head:
        print(head.data,end=' ')
        head=head.next
def rotate_list(head,k):

    new_head = head
    for _ in range(k):
        new_head=new_head.next
    if new_head==None:
        return  head
    temp = new_head
    while temp.next :
        temp = temp.next
    for _ in range(k):
        temp.next = head
        temp = temp.next
        head = head.next
    temp.next = None

    return new_head

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,val):
        node = Node(val)
        if self.head is None:
            self.head=node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
if __name__ == '__main__':
    l = LinkedList()
    ar =[1, 2, 3, 4, 5, 6, 7, 8]
    for a in ar:
        l.insert(a)
    show(l.head)
    print('\nAfter rotaion: ')
    head = rotate_list(l.head,8) # left shift by 3
    show(head)
