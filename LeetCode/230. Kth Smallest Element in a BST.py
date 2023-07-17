class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left=left
        self.right = right
    def insert(self,val):
        if self.val<val:
            if self.right:
                self.right.insert(val)
            else:
                self.right=TreeNode(val)
        else:
            if self.left:
                self.left.insert(val)
            else:
                 self.left= TreeNode(val)
k=1

ans=0
def inorder(root):
    global k,ans
    if root.left :
         inorder(root.left)
    if k==1:
        ans = root.val
    k-=1
    if root.right :
        inorder(root.right)
if __name__ == '__main__':
    root = TreeNode(3)
    root.insert(1)
    root.insert(4)
    root.insert(2)
    inorder(root)
    print(ans,'xxx')