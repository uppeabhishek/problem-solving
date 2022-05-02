# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, level, result):
        if root is None:
            return
        
        if self.prev_level == level:
            result.append(root.val)
            self.prev_level += 1
            
        self.helper(root.right, level + 1, result)
        self.helper(root.left, level + 1, result)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.prev_level = 0
        self.helper(root, 0, result)
        return result
            