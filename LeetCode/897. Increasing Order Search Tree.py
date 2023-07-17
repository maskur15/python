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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def insert(root,val):
    node = TreeNode(val)
    if root is None:
        return node
    else:
        if root.right:
            root.right= insert(root.right,val)
    return root
new_root= None
last_node = None
ar=[]
def inorder(root):
    global new_root,last_node
    if root.left:
        inorder(root.left)
    #ar.append(root.val)
    if new_root is None:
        new_root = TreeNode(root.val)
        last_node=new_root
    else:
        last_node.right = TreeNode(root.val)
        last_node= last_node.right
    if root.right:
        inorder(root.right)
if __name__ == '__main__':
    root = Node(54)
    root.insert(34)
    root.insert(46)
    root.insert(12)
    root.insert(23)
    root.insert(5)
    print('inorder : ')
    inorder(root)
    print(ar)
    # for v in ar:
    #     if new_root is None:
    #         new_root=TreeNode(v)
    #         continue
    #     temp= new_root
    #     while temp.right:
    #         temp=temp.right
    #     temp.right=TreeNode(v)
    while new_root:
        print(new_root.val)
        new_root=new_root.right