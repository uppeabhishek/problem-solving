# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, preorder, inorder_dictionary, left, right):
        if left > right:
            return None

        root = TreeNode(preorder[self.index])
        index = inorder_dictionary[preorder[self.index]]
        self.index += 1
        root.left = self.helper(preorder, inorder_dictionary, left, index - 1)
        root.right = self.helper(preorder, inorder_dictionary, index + 1, right)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        inorder_dictionary = collections.defaultdict(int)

        for i, ele in enumerate(inorder):
            inorder_dictionary[ele] = i

        return self.helper(preorder, inorder_dictionary, 0, len(preorder) - 1)
        
