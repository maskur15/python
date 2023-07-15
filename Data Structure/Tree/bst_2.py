#   https://www.tutorialspoint.com/data_structures_algorithms/binary_search_tree.htm
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def insert(self,data):
        if self.val:
            if self.val<data:
                if self.right is None:
                    self.right= Node(data)
                else:
                    self.right.insert(data)
            else:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
    def search(self,data):
        if self.val == data:
            return True
        if data > self.val:
            if self.right:
                return self.right.search(data)
            else:
                return False
        else:
            if self.left:
                return self.left.search(data)
            else:
                return False
if __name__ == '__main__':
    root = Node(15)
    root.insert(12)
    root.insert(19)
    root.insert(3)
    root.insert(10)
    root.insert(45)
    print(root.search(19))
    print(root.search(2))