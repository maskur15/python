class BinaryTreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(root,val):
    '''insert in a binary search Tree '''
    if root==None:
        root=BinaryTreeNode(val)
        return root
    if root.val<val:
        if root.right==None:
            root.right=BinaryTreeNode(val)
            return root
        else:
           return insert(root.right,val)
    else:
        if root.left==None:
            root.left=BinaryTreeNode(val)
            return root
        else:
            return insert(root.left,val)

def inorder(root):
    if root==None:
        return
    if root.left:
        inorder(root.left)
    print(root.val)
    if root.right:
        inorder(root.right)
height=0
def getHeightofAValue(root,val):
    global height
    if root==None:
        return -1
    left_height =  getHeightofAValue(root.left,val)
    right_height=getHeightofAValue(root.right,val)
    ans= 1+max(left_height,right_height)
    print(ans)
    if val==root.val:
        height=ans
    return ans

def getheight(node):
    if node is None:
        return -1
    else:
        # Compute the height of each subtree
       left=getheight(node.left)
       right=getheight(node.right)
       return 1+max(left,right)
def getNodeHeight(root,val):
    '''using queue and use bfs to calculate the height as level order'''
    q=[]
    if root==None:
        return -1
    depth=0
    level=0
    q.append(root)
    while q:
        n=len(q)
        for _ in range(n):
            front_node= q.pop(0)
            if front_node.val==val:
                depth=level
            if front_node.left:
                q.append(front_node.left)
            if front_node.right:
                q.append(front_node.right)
        level+=1
    return level-depth-1,depth

if __name__ == '__main__':

    root= BinaryTreeNode(5)
    root.left=BinaryTreeNode(10)
    root.right=BinaryTreeNode(15)
    root.left.left=BinaryTreeNode(20)
    root.left.right=BinaryTreeNode(25)
    root.left.right.right=BinaryTreeNode(45)
    root.right.left=BinaryTreeNode(30)
    root.right.right=BinaryTreeNode(35)
    print(getNodeHeight(root,15))
    _=9
    print(_)

