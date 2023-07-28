
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
def insert(root,val):
    if root.val<val:
        if root.right:
            insert(root.right,val)
        else:
            root.right = TreeNode(val)
    else:
        if root.left:
            insert(root.left,val)
        else:
            root.left=TreeNode(val)
    #return root
if __name__ == '__main__':
    ar=list(map(int,input().split()))
    root=TreeNode(ar[0])
    for v in ar[1:]:
        insert(root,v)
    preorder(root)

