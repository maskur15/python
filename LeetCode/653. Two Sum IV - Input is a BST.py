class TreeNode:
    '''Binary search treee'''
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
def insert(root,val):
    temp=root
    node=TreeNode(val)
    if root==None:
        root=node
    if root.val<val:
        if root.right==None:
            root.right=node
        else:
            insert(root.right,val)
    else:
        if root.left==None:
            root.left=node
        else:
            insert(root.left,val)
    return root
def insert_usingStack(root,val):
    temp=root
    node = TreeNode(val)
    while True:
        if temp.val<val:
            if temp.right==None:
                temp.right=node
                break
            else:
                temp=temp.right
        else:
            if temp.left==None:
                temp.left=node
                break
            else:
                temp=temp.left

isPresent={}
ans=False
def inorder(root,target):
    global ans
    if root.left:
        inorder(root.left,target)
    num=target-root.val
    if num in isPresent:
        print(num,root.val)
        ans=True
    else:
        isPresent[root.val]=1

    if root.right:
        inorder(root.right,target)
if __name__ == '__main__':
    root=TreeNode(5)
    # root=insert(root,10)
    # root=insert(root,3)
    # root = insert(root, 1)
    # root = insert(root, 4)
    # root=insert(root,6)
    # root=insert(root,9)
    insert_usingStack(root,10)
    insert_usingStack(root,3)
    insert_usingStack(root,1)
    insert_usingStack(root,9)
    insert_usingStack(root,6)
    insert_usingStack(root,13)
    inorder(root,1)