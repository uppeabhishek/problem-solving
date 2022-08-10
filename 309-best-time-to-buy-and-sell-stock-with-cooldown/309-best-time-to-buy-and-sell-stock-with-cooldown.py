class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def top_dp(i, stockHold):
            
            if i >= len(prices):
                return 0
        
            doNothing, buyStock, sellStock = top_dp(i + 1, stockHold), 0, 0
            
            first, second = 0, 0
            
            if stockHold:
                sellStock = prices[i] + top_dp(i + 2, False)
                first = max(doNothing, sellStock)
            else:
                buyStock = -prices[i] + top_dp(i + 1, True)
                second = max(doNothing, buyStock)
                        
            return max(first, second)
        
        
        
        return top_dp(0, False) 