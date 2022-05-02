# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, new_root):
        if root is None:
            new_root = None
            return new_root
        
        new_root = TreeNode(root.val)
        new_root.left = self.helper(root.right, new_root.left)
        new_root.right = self.helper(root.left, new_root.right)
        return new_root
        
      
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new_root = None
        return self.helper(root, new_root)
