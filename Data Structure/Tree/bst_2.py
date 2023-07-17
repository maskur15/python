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
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val,end=' ')
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.val,end=' ')
        if self.left:
          self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        print(self.val,end=' ')
def inorderUsingStack(root):
    stack=[]
    while root or stack:
        while root:
            stack.append(root)
            root= root.left
        if stack:
            root = stack.pop()
            print(root.val,end=' ')
            root=root.right

if __name__ == '__main__':
    root = Node(54)
    root.insert(34)
    root.insert(46)
    root.insert(12)
    root.insert(23)
    root.insert(5)

    print('inorder : ')
    root.inorder()
    print('\npreorder : ')
    root.preorder()
    print('\npost order : ')
    root.postorder()
    print('\ninorder:')
    inorderUsingStack(root)
