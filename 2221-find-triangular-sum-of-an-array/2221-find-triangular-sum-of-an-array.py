class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        prev, current = nums, []
        
        while len(prev) != 1:
            
            for i in range(len(prev) - 1):
                current.append((prev[i] + prev[i + 1]) % 10)
            
            prev = current
            current = []
        
        return prev[0]
        