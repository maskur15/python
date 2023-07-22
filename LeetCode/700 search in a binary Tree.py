class TreeNode:
    def  __init__(self,val):
        self.val=val
        self.left =None
        self.right=None
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
                self.left=TreeNode(val)
def inorder(root):
    if root==None:
        return None
    if root.left:
        inorder(root.left)
    print(root.val)
    if root.right:
        inorder(root.right)
def search(root,val):
    if root==None:
        return root
    if root.val ==val:
        return root
    if root.val<val:
        return search(root.right,val)
    else:
        return search(root.left,val)
def searchUsingStack(root,val):
    while root:
        if root.val==val:
            break
        if root.val<val:
            root=root.right
        else:
            root=root.left
    return root


if __name__ == '__main__':

    root=TreeNode(4)
    root.insert(2)
    root.insert(7)
    root.insert(1)
    root.insert(3)


    new=search(root,2)
    inorder(new)