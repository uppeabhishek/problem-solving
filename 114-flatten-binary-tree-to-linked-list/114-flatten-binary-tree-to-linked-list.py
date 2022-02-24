# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, prev):
        if root is None:
            return
        
        self.helper(root.right, prev)
        self.helper(root.left, prev)
        
        root.right = self.result
        root.left = None
        self.result = root
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.result = None
        self.helper(root, None)
        return self.result
        
