# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rightSideViewHelper(self, root, result, level):
        if root is None:
            return
        
        if self.prev_level == level:
            result.append(root.val)
            self.prev_level += 1
            
        self.rightSideViewHelper(root.right, result, level + 1)
        self.rightSideViewHelper(root.left, result, level + 1)
        
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.prev_level = 1
        self.rightSideViewHelper(root, result, 1)
        return result