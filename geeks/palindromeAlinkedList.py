from random import  randrange
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def appendFront(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self,data):
        '''This method will apend value at the end of the linked list'''
        node = Node(data)
        if self.head is None:
            self.head= node
            self.tail = node
            return
        self.tail.next= node
        self.tail= node
    def showList(self):
        if self.head is None: return
        current = self.head
        while current:
            print(current.data,end=' ')
            current=current.next
        print()
    def length(self):
        current = self.head
        c=0
        while current:
            c+=1
            current = current.next
        return  c


class Solution:

    def length(self,head):
        current = head
        c=0
        while current:
            c+=1
            current = current.next
        return  c
    def isPalindrome(self,head):
        ln = self.length(head)
        if ln <=1:
            return True
        rev = LinkedList()
        current = head
        i= ln//2
        while current:
            if i==0:
                break
            i-=1
            temp = Node(current.data)
            temp.next = rev.head
            rev.head = temp
            current = current.next

        if ln%2==1 and current:
            current = current.next
        temp = rev.head
        while current and temp:
            if current.data==temp.data:
                current=current.next
                temp=temp.next
            else:
                return False
        return True



if __name__ == '__main__':
    L = LinkedList()


    L.showList()
    s = Solution()
    print(s.isPalindrome(L.head))

