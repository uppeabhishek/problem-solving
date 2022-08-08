# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBSTHelper(self, root, left, right):
        if root is None:
            return True
        
        if root.val >= left or root.val <= right:
            return False
        
        return self.isValidBSTHelper(root.left, root.val, right) and self.isValidBSTHelper(root.right, left, root.val)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, sys.maxsize, -sys.maxsize)