class Node:
    def __init__(self,data):
        self.value =data
        self.left = None
        self.right = None

def inorder(root):
    if root is not None :
        inorder(root.left)
        print(str(root.value)+'>',end=' ')
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.value:
        node.left = insert(node.left,key)
    else:
        node.right= insert(node.right,key)
    return node
if __name__ == '__main__':
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 14)
    root = insert(root, 4)
    inorder(root)