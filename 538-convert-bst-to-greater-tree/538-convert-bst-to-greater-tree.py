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
        
        self.helper(root.right)
        root.val = root.val + self.result
        self.result = root.val
        self.helper(root.left)
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.result = 0
        self.helper(root)
        return root