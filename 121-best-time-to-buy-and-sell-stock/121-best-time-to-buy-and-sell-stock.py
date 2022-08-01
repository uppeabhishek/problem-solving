class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        result = 0
        
        for i in range(1, len(prices)):
            if prices[i] > current_min:
                result = max(result, prices[i] - current_min)
            
            current_min = min(current_min, prices[i])
    
        return result
            