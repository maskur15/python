#insertion in a binary search tree
#where each left node is less than its parent node
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    parent_node=None
    current_node=root
    while current_node!= None:
        parent_node=current_node
        if key > current_node.val:
            current_node=current_node.right
        else:
            current_node=current_node.left
    if key<parent_node.val:
        Node(parent_node.left,key)
    else:
        Node(parent_node.right,key)