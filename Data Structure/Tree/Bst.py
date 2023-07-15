
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def insert(root,val):
    node = Node(val)
    if root is None:
       root=node
       return root
    else:
        if val > root.val:
            root.right = insert(root.right,val)
        else:
            root.left = insert(root.left,val)
        return root
def show(root):
    if root is None:
        return None
    if root.left==None and root.right==None:
        print(root.val)
    if root.left:
        (show(root.left))
    if root.right:
        (show(root.right))
def search(root,num):
    if root is None :
        return False
    if root.val == num:
        return  True
    if root.val < num:
        return search(root.right,num)
    else:
        return search(root.left,num)

if __name__ == '__main__':
    root = None
    root = insert(root,20)
    root= insert(root,15)
    root = insert(root,40)
    root= insert(root,5)
    root= insert(root,25)
    root= insert(root,45)
    show(root)
    print(search(root,45))