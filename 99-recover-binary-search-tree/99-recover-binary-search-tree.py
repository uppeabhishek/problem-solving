# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def swap(self, root1, root2):
        temp = root1.val
        root1.val = root2.val
        root2.val = temp
        
    def helper(self, root):
        if root is None:
            return
        
        self.helper(root.left)
                
                
        if self.prev is None:
            self.prev = root
        else:
            if not self.swapped_node:
                if self.prev.val > root.val:
                    self.swapped_node = self.prev
                    self.second_swapped_node = root
            else:
                if self.swapped_node.val > root.val:
                    self.second_swapped_node = root 
            self.prev = root
        
        self.helper(root.right)
        
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.swapped_node = None
        self.second_swapped_node = None
        
        self.helper(root)
        self.swap(self.swapped_node, self.second_swapped_node)
        
        return root