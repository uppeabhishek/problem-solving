# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalancedHelper(self, root):
        if root is None:
            return 0
        
        left = self.isBalancedHelper(root.left)
        
        right = self.isBalancedHelper(root.right)
        
        if abs(left - right) > 1:
            self.result = False
            return 0
            
        return 1 + max(left, right)
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        self.isBalancedHelper(root)
        
        return self.result