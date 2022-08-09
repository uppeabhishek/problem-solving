# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSumHelper(self, root, targetSum, currentArray, dictionary):
        
        if root is None:
            return
        
        value = root.val
        
        if len(currentArray):
            value += currentArray[-1]
        
        currentArray.append(value)

        if value == targetSum:
            self.cnt += 1
        
        if value - targetSum in dictionary:
            self.cnt += dictionary[value - targetSum]
        
        dictionary[value] += 1
                
        self.pathSumHelper(root.left, targetSum, currentArray, dictionary)
        self.pathSumHelper(root.right, targetSum, currentArray, dictionary)
        
        lastValue = currentArray[-1]
        
        dictionary[lastValue] -= 1
        
        if dictionary[lastValue] == 0:
            del dictionary[lastValue]
        
        currentArray.pop()
        
        
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if root is None:
            return 0
        
        currentArray = []
        dictionary = defaultdict(int)
        self.cnt = 0
        self.pathSumHelper(root, targetSum, currentArray, dictionary)
        
        return self.cnt