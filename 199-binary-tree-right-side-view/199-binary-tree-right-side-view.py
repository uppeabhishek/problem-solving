# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rightSideViewHelper(self, root, result, level, visited):
        if root is None:
            return
        
        if level not in visited:
            result.append(root.val)
            visited.add(level)
        
        self.rightSideViewHelper(root.right, result, level + 1, visited)
        
        self.rightSideViewHelper(root.left, result, level + 1, visited)
        
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        visited = set()
        self.rightSideViewHelper(root, result, 1, visited)
        return result