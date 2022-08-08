# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def invertTreeHelper(self, root):
        if root is None:
            return
        
        self.invertTreeHelper(root.left)
        self.invertTreeHelper(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
                
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeHelper(root)
        
        return root