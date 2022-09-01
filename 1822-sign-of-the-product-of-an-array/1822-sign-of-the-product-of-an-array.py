class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        neg = 0
        
        for num in nums:
            if not num:
                return 0
            
            if num < 0:
                neg += 1
        
        return 1 if neg & 1 == 0 else -1