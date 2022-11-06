# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python.leetcode.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def helper(root):

            if root is None:
                return 0

            if root.left is None and root.right is None:
                return root.val

            left = helper(root.left)

            right = helper(root.right)

            root.val = root.val + max(left, right)

            return root.val

        helper(root)

        print(root)


s = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

s.maxPathSum(root)
