# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque([])
        
        result = []
        
        while True:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
                continue
            
            if not len(stack):
                break
            
            top = stack.pop()
                                
            if top.right:
                root = top.right
        
        return result