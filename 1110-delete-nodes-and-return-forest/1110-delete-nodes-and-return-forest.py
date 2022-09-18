# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        result = []
        
        def postorder(root, parent):
            
            nonlocal to_delete, result
            
            if root is None:
                return 
            
            postorder(root.left, root)
            postorder(root.right, root)
            
            if root.val in to_delete:
                
                if root.left:
                    result.append(root.left)
                
                if root.right:
                    result.append(root.right)
                
                if parent.left and parent.left.val == root.val:
                    parent.left = None
                    
                if parent.right and parent.right.val == root.val:
                    parent.right = None
                                
        
        if root.val in to_delete:
            postorder(root.left, root)
            postorder(root.right, root)
            if root.left:
                result.append(root.left)
            if root.right:
                result.append(root.right)
        else:
            postorder(root, None)
            result.append(root)
        
        return result