class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left=left
        self.right = right
    def insert(self,val):
        if val>self.val:
            if self.right==None:
                self.right= TreeNode(val)
            else:
                self.right.insert(val)
        else:
            if self.left==None:
                self.left= TreeNode(val)
            else:
                self.left.insert(val)
def inorder(root):
    global  result,low,high
    if root.left:
        inorder(root.left)
    if root.val >=low and root.val<=high:
        result+=root.val
    #print(root.val)
    if root.right:
        inorder(root.right)

def sumbst(root, low, high):
    if root==None:
        return 0
    if  root.val<low:
        return sumbst(root.right,low,high)
    if root.val>high:
        return sumbst(root.left,low,high)
    return root.val+ sumbst(root.left,low,high) + sumbst(root.right,low,high)



if __name__ == '__main__':
    root = TreeNode(10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    root.insert(18)
    result = 0
    low=7
    high = 15
    inorder(root)
    print(result)
    print(sumbst(root,7,15))
