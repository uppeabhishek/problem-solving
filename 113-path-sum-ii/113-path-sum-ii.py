# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import copy
class Solution:
    
    def pathSumHelper(self, root, targetSum, tempResult, result):
        if root is None:
            return 
        
        tempResult.append(root.val)

        if root.left is None and root.right is None:
            if targetSum - root.val == 0:
                result.append(copy(tempResult))
        
        self.pathSumHelper(root.left, targetSum - root.val, tempResult, result)
        self.pathSumHelper(root.right, targetSum - root.val, tempResult, result)
        
        tempResult.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        tempResult = []
        
        self.pathSumHelper(root, targetSum, tempResult, result)
        
        return result