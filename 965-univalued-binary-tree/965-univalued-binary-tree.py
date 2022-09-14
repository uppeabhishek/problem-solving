# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, parent):
            
            if root is None:
                return True
            
            
            if parent is not None:
                if root.val != parent.val:
                    return False
                
            left = helper(root.left, root)
            
            if not left:
                return False
            
            right = helper(root.right, root)
            
            if not right:
                return False
        
            return True
        
        return helper(root, None)