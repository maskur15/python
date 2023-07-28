class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def insert(root,val):
    if root==None:
        return TreeNode(val)
    if root.val<val:
        root.right=insert(root.right,val)
    else:
        root.left=insert(root.left,val)
    return root
def inorder(root):
    if root.left:
        inorder(root.left)
    print(root.val,end=' ')
    if root.right:
        inorder(root.right)
def invert(root):
    if root==None:
        return
    temp=root.left
    root.left=root.right
    root.right=temp
    invert(root.left)
    invert(root.right)

def leveLorder(root):
    if root==None:
        return
    else:
        q=[]
        q.append(root)
        while len(q)>=1:
            root=q.pop(0)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            print(root.val,end=' ')



if __name__ == '__main__':
    root=TreeNode(4)
    insert(root,2)
    insert(root,7)
    insert(root,1)
    insert(root,3)
    insert(root,6)
    insert(root,9)

    leveLorder(root)
    print()
    invert(root)
    leveLorder(root)
