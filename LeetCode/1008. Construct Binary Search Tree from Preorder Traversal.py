
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def preorder(root):
    print(root.val)
    if  root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)
def insert(root=None,val=0):
    if root==None:
        root=val
        return root
    if root.val<val:
        if root.right:
            return  insert(root.right,val)
        else:
            root.right = TreeNode(val)
    else:
        if root.left:
            return insert(root.left,val)
        else:
            root.left=TreeNode(val)
    return root
if __name__ == '__main__':
    root=TreeNode
    root=insert(root,10)