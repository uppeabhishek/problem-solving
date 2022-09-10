# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
          
        def swap(root1, root2):
            temp = root1.val
            root1.val = root2.val
            root2.val = temp
        
        prev = None
        
        node1, node2 = None, None
        
        def helper(root):
            
            nonlocal prev, node1, node2
            
            if root is None:
                return
            
            helper(root.left)
            
            if prev:                
                if prev.val > root.val:
                    if not node1:
                        node1 = prev
                        node2 = root
                    else:
                        node2 = root
            
            prev = root
            
            helper(root.right)
            
        
        helper(root)
        
        swap(node1, node2)
            