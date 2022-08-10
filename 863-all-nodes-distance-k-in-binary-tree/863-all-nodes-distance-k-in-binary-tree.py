# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    
        def setParent(root, parent):
            
            if root is None:
                return 
            
            root.parent = parent
            
            setParent(root.left, root)
            setParent(root.right, root)
    
        
        setParent(root, None)
        
        
        def BFS():
            queue = deque([(target, 0)])
            cache = set()
            
            result = []
            
                        
            while len(queue):
                
                top, distance = queue.popleft()
                
                cache.add(top)
                
                if distance == k:
                    result.append(top.val)
                
                new_distance = distance + 1
                
                if top.left and top.left not in cache:
                    queue.append((top.left, new_distance))
                
                if top.right and top.right not in cache:
                    queue.append((top.right, new_distance))
                    
                if top.parent and top.parent not in cache:
                    queue.append((top.parent, new_distance))
                
            
            return result
        
        return BFS()
                    
                    
                
                
                
            
            
            
        
        
            
            
    