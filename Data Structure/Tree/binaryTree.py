class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.value=data
    def preOrderTraverse(self):
        print(self.value,end= ' ')
        if self.left:
            self.left.preOrderTraverse()
        if self.right:
            self.right.preOrderTraverse()
    def inOrderTraverse(self):
        if self.left:
            self.left.inOrderTraverse()
        print(self.value,end=' ')
        if self.right:
            self.right.inOrderTraverse()
    def postOrderTraverse(self):
        if self.left:
            self.left.postOrderTraverse()
        if self.right:
            self.right.postOrderTraverse()
        print(self.value,end=' ')

if __name__ == '__main__':
    root=Node(4)
    root.left=Node(5)
    root.right=Node(9)
    root.left.left=Node(2)
    root.left.right=Node(3)
    print('preorder Travere: ')
    root.preOrderTraverse()
    print('\nIn order Traverse: ')
    root.inOrderTraverse()
    print('\n Post order Traverse')
    root.postOrderTraverse()