# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        min_level = sys.maxsize
        max_level = -sys.maxsize
        
        queue = deque([(root, 0, 0)])
        
        while len(queue):
            top, row, column = queue.popleft()
                        
            min_level = min(min_level, column)
            max_level = max(max_level, column)
              
            dic[column].append((top.val, row, column))
            
            if top.left:
                queue.append((top.left, row + 1, column - 1))
            
            if top.right:
                queue.append((top.right, row + 1, column + 1))
                
        result = []
                
        for i in range(min_level, max_level + 1):
            result.append(dic[i])
        
        for i1, ele in enumerate(result):
            i = 0
            while i < len(ele) - 1:
                if ele[i][1] == ele[i + 1][1] and ele[i][2] == ele[i + 1][2]:
                    prev = i
                    while i < len(ele) - 1 and ele[i][1] == ele[i + 1][1] and ele[i][2] == ele[i + 1][2]:
                        i += 1
                    result[i1] = result[i1][0:prev] + sorted(result[i1][prev:i+1], key=lambda k:k[0]) + result[i1][i+1:]
                else:
                    i += 1
        
        final_result = []
        
        for ele in result:
            temp = []
            for ele1 in ele:
                temp.append(ele1[0])
            final_result.append(temp)
            
        return final_result