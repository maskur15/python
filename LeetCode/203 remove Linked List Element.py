class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def remove_value(head,value):
    new_head = None
    while head:
        if head.val ==value:
            pass
        else:
            if new_head is None:
                new_head= ListNode(head.val)
            else:
                temp = new_head
                while temp.next:
                    temp = temp.next
                temp.next = ListNode(head.val)
        head = head.next
    return new_head
def show_usingHead(head):
    while head:
        print(head.val,end=' ')
        head = head.next

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,val):
        node = ListNode(val)
        if self.head==None:
            self.head = node
            self.tail = node
        else:
            self.tail.next=node
            self.tail = node
    def show_list(self):
        temp = self.head
        while temp:
            print(temp.val,end=' ')
            temp = temp.next

    def remove(self,val):

        while self.head and  self.head.val == val:
            self.head = self.head.next
        if self.head is None:
            return  self.head

        pre = self.head
        temp = self.head.next

        while temp:
            if temp.val ==val:
                pre.next = temp.next
                temp = temp.next
            else:
                pre = temp
                temp =temp.next
        return self.head



if __name__ == '__main__':
    l = LinkedList()
    l.insert(1)
    l.insert(3)
    l.insert(6)
    l.insert(4)
    l.insert(1)
    l.insert(3)

    l.show_list()
    print("\nRemove 1 : ")
    head = remove_value(l.head,1)
    show_usingHead(head)