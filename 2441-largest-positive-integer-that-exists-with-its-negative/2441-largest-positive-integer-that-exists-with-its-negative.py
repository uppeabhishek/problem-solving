class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        
        nums.sort(reverse = True)
        
        for num in nums:
            if num < 0:
                break
            
            if -num in c:
                return num
        
        return -1