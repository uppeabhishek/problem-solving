# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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