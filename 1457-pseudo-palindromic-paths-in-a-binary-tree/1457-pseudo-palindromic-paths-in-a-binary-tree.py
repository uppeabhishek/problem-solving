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
        result = 0
        
        def helper(root):
            
            nonlocal result
            
            if root is None:
                return 
            
            if root.left is None and root.right is None:
                odd_cnt = 0
                
                cache[root.val] += 1
                
                for _, value in cache.items():
                    if value & 1 == 1:
                        odd_cnt += 1

                    if odd_cnt > 1:
                        break
                
                cache[root.val] -= 1
                
                if odd_cnt < 2:
                    result += 1
                    
                return
            
            array.append(root.val)
            cache[root.val] += 1

            helper(root.left)
            helper(root.right)
              
            cache[array[-1]] -= 1
            array.pop()
            
        helper(root)
        
        return result
        