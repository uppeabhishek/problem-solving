# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestorHelper(self, root, p, q):
        if root == p or root == q:
            return root
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorHelper(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorHelper(root.right, p, q)
        
        return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowestCommonAncestorHelper(root, p, q)