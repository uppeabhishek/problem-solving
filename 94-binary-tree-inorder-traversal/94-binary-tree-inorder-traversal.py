# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        
        result = []
        
        while True:
            if root:
                stack.append(root)
                root = root.left
                continue
                 
            top = None
            
            if len(stack):
                top = stack.pop()
                result.append(top.val)
            
            if top and top.right:
                root = top.right
            elif not len(stack):
                break
    
        return result
    
        