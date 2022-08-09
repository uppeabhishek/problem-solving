# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSumHelper(self, root, targetSum):
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            if targetSum - root.val == 0:
                return True
            return False
        
        left = self.hasPathSumHelper(root.left, targetSum - root.val)
        right = self.hasPathSumHelper(root.right, targetSum - root.val)
        
        return left or right
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.hasPathSumHelper(root, targetSum)