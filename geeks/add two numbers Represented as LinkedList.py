class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail=node

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
def show(head:Node):
    """

    :type head: object
    """
    print()
    while head:
        print(head.data,end=' ')
        head = head.next
def reverse(head:Node):
    ln =0
    new_head = None
    while head:
        node = Node(head.data)
        ln+=1
        if new_head is None:
            new_head = node
        else:
            node.next = new_head
            new_head = node
        head = head.next
    return  new_head,ln
def insert_pre(head,val):
    node = Node(val)
    node.next = head
    return node

def sum(h1,h2):
    new_head = None
    tail = None
    carry = None
    while h1:
        s = h1.data + h2.data
        if carry: s+=carry

        if s//10>=1:
            carry = s//10
            s= s%10
        else:
            carry =None
        print(s,end=' ')
        new_head= insert_pre(new_head,s)
        h1=h1.next
        h2 = h2.next
    while h2:
        s = h2.data
        if carry: s += carry
        if s // 10 >= 1:
            carry = s // 10
            s = s % 10
        else:
            carry = None
        print(s,end=' ')
        new_head = insert_pre(new_head,s)
        h2=h2.next
    if carry:
        print(carry)
    return new_head

def addTwoLists( first, second):
    from collections import deque
    # code here
    # return head of sum list
    head = None
    s1 = deque()
    s2 = deque()
    s = deque()
    temp1 = first
    temp2 = second
    while temp1 and temp2:
        s1.append(temp1.data)
        s2.append(temp2.data)
        temp1 = temp1.next
        temp2 = temp2.next
    while temp1:
        s1.append(temp1.data)
        temp1 = temp1.next
    while temp2:
        s2.append(temp2.data)
        temp2 = temp2.next
    carry = 0
    while s1 and s2:
        sum = s1.pop() + s2.pop() + carry

        if sum >= 10:
            carry = 1
            sum = sum % 10
        else:
            carry = 0

        s.append(sum)
    while s1:
        sum = s1.pop() + carry
        if sum >= 10:
            carry = 1
            sum = sum % 10
        else:
            carry = 0
        s.append(sum)
    while s2:
        sum = s2.pop() + carry
        if sum >= 10:
            carry = 1
            sum = sum % 10
        else:
            carry = 0
        s.append(sum)
    if carry == 1: s.append(carry)
    last = head
    while s:
        node = Node(s.pop())
        if head:
            last.next = node
            last = node
        else:
            head = node
            last = node
    return head


if __name__ =='__main__':

    l1 = LinkedList()
    l2 = LinkedList()
    ar = list(map(int,input().split()))
    ar2 = list(map(int,input().split()))

    for a in ar2:
        l1.add(a)
    for a in ar:
        l2.add(a)
    head = addTwoLists(l1.head,l2.head)
    print('XXmmmmmm')
    h1,lnth1 =  reverse(l1.head)
    h2,lnth2 = reverse(l2.head)

    print('Sum: \n')
    if lnth1<lnth2:
        head =sum(h1,h2)
    else:
       head = sum(h2,h1)
    show(head)


