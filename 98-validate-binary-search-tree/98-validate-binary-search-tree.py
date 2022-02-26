# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, min_val, max_val):
        if root is None:
            return True
        
        if root.val <= min_val or root.val >= max_val:
            return False
        
        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -math.inf, math.inf)