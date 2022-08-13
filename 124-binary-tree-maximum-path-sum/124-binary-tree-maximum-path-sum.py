# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
                  
        max_val = -sys.maxsize
        
        def helper(root):
            
            nonlocal max_val
                        
            if root is None:
                return 0
                        
            left = max(helper(root.left), 0)
            
            right = max(helper(root.right), 0)
            
            max_val = max(max_val, left + right + root.val)
            
            return root.val + max(left, right)
    
        
        helper(root)
        
        return max_val
        