# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from python.leetcode.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        dic = {}

        for i in range(len(inorder)):
            dic[inorder[i]] = i

        n = len(preorder)

        def construct(index, left, right):

            if left > right:
                return None

            current = preorder[index]

            root = TreeNode(current)

            root.left = construct(index + 1, left, dic[current] - 1)

            root.right = construct(index + 1, dic[current] + 1, right)

            return root

        return construct(0, 0, n - 1)


s = Solution()
s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
