class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @cache
        def top_dp(i, k, stockHold):
            
            if i == len(prices) or k == 0:
                return 0
        
            doNothing, buyStock, sellStock = top_dp(i + 1, k, stockHold), 0, 0
            
            first, second = 0, 0
            
            if stockHold:
                sellStock = prices[i] + top_dp(i + 1, k - 1, False)
                first = max(doNothing, sellStock)
            else:
                buyStock = -prices[i] + top_dp(i + 1, k, True)
                second = max(doNothing, buyStock)
                        
            return max(first, second)
        
        
        
        return top_dp(0, k, False) 
            
            
            