class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def helper(current, left, right):
            
            nonlocal result
            
            if left == n and right == n:
                result.append(current)
                return
                        
            if left != n:
                helper(current + "(", left + 1, right)
            
            if left > right:
                helper(current + ")", left, right + 1)
        
        helper("", 0, 0)
        
        
        return result
            
            
            