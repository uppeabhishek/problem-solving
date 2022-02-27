# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addMinMax(self, level, min_dic, max_dic, val):
        if level in min_dic:
            min_dic[level] = min(val, min_dic[level])
        else:
            min_dic[level] = val
            
        if level in max_dic:
            max_dic[level] = max(val, max_dic[level])
        else:
            max_dic[level] = val 
        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0, 0)])
        min_dic = {}
        max_dic = {}
        
        while len(queue):
            top, value, level  = queue.popleft()
            
            if top.left:
                val = 2 * value + 1
                queue.append((top.left, val, level + 1))
                self.addMinMax(level + 1, min_dic, max_dic, val)
                
            if top.right:
                val = 2 * value + 2
                queue.append((top.right, val, level + 1))
                self.addMinMax(level + 1, min_dic, max_dic, val)
            
        result = 1
                
        for ele in min_dic:
            if ele in max_dic:
                result = max(result, max_dic[ele] - min_dic[ele] + 1)
                
        return result
            