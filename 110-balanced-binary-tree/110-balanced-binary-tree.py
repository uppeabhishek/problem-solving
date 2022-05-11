# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if abs(left - right) > 1:
            self.res = False
            return abs(left - right)
        
        return 1 + max(left, right)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.helper(root)
        return self.res