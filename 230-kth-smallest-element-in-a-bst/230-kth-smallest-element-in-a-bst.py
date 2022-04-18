# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, k):
        if root is None:
            return

        self.helper(root.left, k)
    
        
        if self.cnt == k and self.result is None:
            self.result = root.val
            return
    
        self.cnt += 1

        self.helper(root.right, k)

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.cnt = 1
        self.helper(root, k)
        return self.result