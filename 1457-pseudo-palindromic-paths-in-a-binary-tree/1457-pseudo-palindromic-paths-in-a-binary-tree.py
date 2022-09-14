# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        cache = defaultdict(int)
        array = []
        counter = [0, 0]
        result = 0
        
        def updateCache(val, addition = True):
            if addition:
                if val not in cache:
                    counter[0] += 1
                    cache[val] += 1
                else:
                    cache[val] += 1
                    if cache[val] & 1 == 0:
                        counter[0] -= 1
                        counter[1] += 1
                    else:
                        counter[0] += 1
                        counter[1] -= 1
            else:
                cache[val] -= 1
                if cache[val] & 1 == 0:
                    counter[0] -= 1
                    counter[1] += 1
                else:
                    counter[0] += 1
                    counter[1] -= 1
        
        def helper(root):
            
            nonlocal result
            
            if root is None:
                return 
            
            if root.left is None and root.right is None:                
                
                updateCache(root.val)
                
                if counter [0] < 2:
                    result += 1
                
                updateCache(root.val, False)
                    
                return
            
            array.append(root.val)
            updateCache(root.val)

            helper(root.left)
            helper(root.right)
              
            updateCache(array[-1], False)
            array.pop()
            
        helper(root)
                
        return result
        