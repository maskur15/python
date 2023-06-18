class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class MyStack:
    head = None
    def push(self,data):
        node = StackNode(data)
        node.next = self.head
        self.head = node
    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        else: return -1
    def isEmpty(self):
        if self.head is None: return  True
        return  False
if __name__ == '__main__':
    s = MyStack()
    s.push(3)
    s.push(5)
    s.push(8)
    s.push(1)
    while s:
        print(s.pop())
        print(s)

    print(s.isEmpty())
