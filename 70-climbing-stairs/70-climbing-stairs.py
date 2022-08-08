class Solution:
    
    
    def climbStairsHelper(self, n: int, dic) -> int:
        if n in dic:
            return dic[n]
        
        if n == 1 or n == 0:
            return 1
        
        dic[n] = self.climbStairsHelper(n - 1, dic) + self.climbStairsHelper(n - 2, dic)
        return dic[n]
    
    def climbStairs(self, n: int) -> int:
        dic = {}
        return self.climbStairsHelper(n, dic)