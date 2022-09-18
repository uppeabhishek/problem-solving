# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def longestCommonAncestor(root):
            
            if root is None:
                return None
            
            if root.val == startValue or root.val == destValue:
                return root
                        
            left = longestCommonAncestor(root.left)
                        
            right = longestCommonAncestor(root.right)
                        
            if left and right:
                return root
            
            if left:
                return left
            
            if right:
                return right
            
            return None
        
        
        lowest = longestCommonAncestor(root)
        
        def getPath(val, root, path):
            
            if root is None:
                return False
            
            if root.val == val:
                return True
            
            left = getPath(val, root.left, path)
            right = getPath(val, root.right, path)
            
            if left:
                path.append("L")
                return True
            
            if right:
                path.append("R")
                return True
            
            return False
    
        
        path1, path2 = [], []
        
        getPath(startValue, lowest, path1)     
        getPath(destValue, lowest, path2)
        
        if not len(path1):
            return "".join(reversed(path2))
        
        
        if not len(path2):
            return "U" * len(path1)
        
        return "U" * len(path1) + "".join(reversed(path2))
        
        