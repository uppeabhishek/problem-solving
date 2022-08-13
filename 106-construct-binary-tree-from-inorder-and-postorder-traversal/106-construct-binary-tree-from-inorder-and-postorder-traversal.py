# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inorder_dict = {}
        
        for i, ele in enumerate(inorder):
            inorder_dict[ele] = i
        
        
        n = len(inorder)
        
        postorder_index = n - 1
        
        def construct(left, right):
            
            nonlocal postorder_index
            
            if left > right:
                return None
                        
            current_postorder_index = postorder[postorder_index]
            
            root = TreeNode(current_postorder_index)
            
            postorder_index -= 1
            
            root.right = construct(inorder_dict[current_postorder_index] + 1, right)
            
            root.left = construct(left, inorder_dict[current_postorder_index] - 1)
            
            return root
    
        return construct(0, n - 1)
            
        
        