# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def inorderSuccessorHelper(self, root, p):
        if root is None:
            return
        
        if root.val > p.val:
            if not self.inorderVal or root.val < self.inorderVal.val:
                self.inorderVal = root
        
        if root.val < p.val:
            self.inorderSuccessorHelper(root.right, p)
        elif root.val > p.val:
            self.inorderSuccessorHelper(root.left, p)
        else:
            self.inorderSuccessorHelper(root.left, p)
            self.inorderSuccessorHelper(root.right, p)

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.inorderVal = None
        self.inorderSuccessorHelper(root, p)
        
        return self.inorderVal