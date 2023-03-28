class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,node):
        if self.head is None:
            self.head = node
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode=lastNode.next
            lastNode.next=node
    def printList(self):

        currentNode = self.head
        if currentNode== None :
            print('empty list ')
            return
        while currentNode is not None:
            print(currentNode.data)
            currentNode=currentNode.next
if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insert(Node(3))
    linkedList.insert(Node(4))
    linkedList.insert(Node(1))
    linkedList.insert(Node(6))
    linkedList.printList()