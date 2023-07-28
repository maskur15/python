
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

def insert(root,pos,ar,mx):
    if pos==len(ar):
        return pos
    if ar[pos]<root.val:
        root.left=TreeNode(ar[pos])
        pos+=1
        pos= insert(root.left,pos,ar,root.val-1)
    if ar[pos]<=mx:
        root.right=TreeNode(ar[pos])
        pos+=1
        pos=insert(root.right,pos,ar,mx)
    return pos
if __name__ == '__main__':
    ar=list(map(int,input().split()))
    root=TreeNode(ar[0])
    insert(root,1,ar,ar[len(ar)-1])
    preorder(root)

