class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def insert(ar):
    if len(ar)==0:
        return None
    if len(ar)==1:
        return TreeNode(ar[0])
    mid=len(ar)//2
    node=TreeNode(ar[mid])
    node.left=insert(ar[:mid])
    if mid+1<len(ar):
         node.right=insert(ar[mid+1:])
    return node
height={}
def getheight(node):
    global height
    if node==None:
        return 0
    if node.left==None and node.right==None:
        height[node.val]=0
        return 0
    left=getheight(node.left)
    right=getheight(node.right)
    height[node.val]=1+max(left,right)
    return 1+max(left,right)
balance_factor={}
def getBalanceFactor(node):
    if node==None:
        return 0
    if node.left==None  and node.right==None:
        balance_factor[node.val]=0
        return 0
    left=getBalanceFactor(node.left)
    right=getBalanceFactor(node.right)
    balance_factor[node.val]=left-right
    return 1+max(left,right)

def preorder(root):
    if root==None:
        return
    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root.left:
        inorder(root.left)
    print(root.val,end=' ')
    if root.right:
        inorder(root.right)
if __name__ == '__main__':
    ar=[3,4,6,7,8,10,12,13]
    root=insert(ar)
    print('inorder: ')
    inorder(root)
    print('\npreorder:')
    preorder(root)
    getheight(root)
    print('\nheight : ',height)

    getBalanceFactor(root)
    print('\nBalance factor: ',balance_factor)
