# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, root):
        if root is None:
            return

        self.helper(root.left)

        if self.result is None:
            self.result = root
            self.current_result = self.result
        else:
            self.current_result.right = root
            self.current_result = self.current_result.right
            self.current_result.left = None

        self.helper(root.right)

        return self.result

    def increasingBST(self, root):
        self.result = None
        self.current_result = None
        return self.helper(root)
