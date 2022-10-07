class Solution:
    def dp():
        n = len(cardPoints)
        
        @cache
        def helper(i, j):  
            
            if j == k:
                return 0
            
            first, second = 0, 0
                        
            first = cardPoints[i] + helper(i + 1, j + 1)
            
            second = cardPoints[(n - 1) - (j - i)] + helper(i, j + 1)
            
            return max(first, second)
        
        return helper(0, 0)
    
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        
        addition = 0
        
        for i in range(n - k, n):
            addition += cardPoints[i]
        
        
        result = addition
        
        for i in range(k):
            
            addition += cardPoints[i]
            addition -= cardPoints[i + n - k]
            
            result = max(result, addition)
        
        return result