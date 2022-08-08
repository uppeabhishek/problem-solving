# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTreeHelper(self, root):
        
        if root is None:
            return 0
        
        left = self.diameterOfBinaryTreeHelper(root.left)
        right = self.diameterOfBinaryTreeHelper(root.right)
                
        self.result = max(self.result, left + right)
        
        return 1 + max(left, right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.diameterOfBinaryTreeHelper(root)
        return self.result