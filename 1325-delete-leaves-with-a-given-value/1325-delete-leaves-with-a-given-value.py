# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, parent, target):
        if root is None:
            return
        
        self.preorder(root.left, root, target)
        self.preorder(root.right, root, target)
            
        if not (root.left or root.right) and parent and root.val == target:
            if parent.left == root:
                parent.left = None
            else:
                parent.right = None
        
        
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.preorder(root, None, target)
        if root.val == target and not (root.left or root.right):
            return None
        return root