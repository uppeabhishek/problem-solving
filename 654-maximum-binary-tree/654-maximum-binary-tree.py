# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxIndex(self, nums, l, r):
        res, ind = -math.inf, -1
        
        for i in range(l, r + 1):
            if nums[i] > res:
                res = nums[i]
                ind = i
                
        return ind
        
    def helper(self, nums, l, r):
        if l > r:
            return None
        
        max_ind = self.getMaxIndex(nums, l, r)
        
        return TreeNode(nums[max_ind], self.helper(nums, l, max_ind - 1), self.helper(nums, max_ind + 1, r));
        
        
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)