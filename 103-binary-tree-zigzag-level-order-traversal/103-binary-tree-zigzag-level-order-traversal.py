# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        queue = deque([(root, 1)])
        result = defaultdict(deque)
        
        while len(queue):
            top, level = queue.popleft()
            
            if level & 1 == 1:
                result[level].append(top.val)
            else:
                result[level].appendleft(top.val)

            if top.left:
                queue.append((top.left, level + 1))
            
            if top.right:
                queue.append((top.right, level + 1))
        
        final_result = []
        
        for _, value in result.items():
            final_result.append(value)
        
        return final_result