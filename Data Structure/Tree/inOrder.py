class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data
class Solution:
    def inorderTraversal(self, root):
        ar = list()
        def inorder(root):
            if root == None:
                return
            if root.left:
                inorder(root.left)
            ar.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        return ar
if __name__ == '__main__':
    root=Node(4)
    root.left=Node(5)
    root.right=Node(9)
    root.left.left=Node(2)
    root.left.right=Node(3)
    s=Solution()
    ar=s.inorderTraversal(root)
    print(ar)