# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python.leetcode.TreeNode import TreeNode


class Solution:

    def __init__(self):
        self.cnt = 0
        self.currentCnt = 0

    def pathSumHelperCount(self, root, targetSum):

        if root is None:
            return

        if targetSum - root.val == 0:
            self.currentCnt += 1

        self.pathSumHelperCount(root.left, targetSum - root.val)
        self.pathSumHelperCount(root.right, targetSum - root.val)

    def pathSumHelper(self, root, targetSum):

        if root is None:
            return

        self.currentCnt = 0

        self.pathSumHelperCount(root, targetSum)

        self.cnt += self.currentCnt

        self.pathSumHelper(root.left, targetSum)
        self.pathSumHelper(root.right, targetSum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        self.pathSumHelper(root, targetSum)
        return self.cnt


s = Solution()

# root = TreeNode(10)
# root.left = TreeNode(5)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(3)
# root.left.left.right = TreeNode(-2)
# root.left.right = TreeNode(2)
# root.left.right.right = TreeNode(1)
# root.right = TreeNode(-3)
# root.right.right = TreeNode(11)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(-1)

root = TreeNode(1)
root.left = TreeNode(-2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(-1)
root.right = TreeNode(-3)
root.right.left = TreeNode(-2)

print(s.pathSum(root, -1))
